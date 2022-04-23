from typing import Any, List, MutableMapping, Optional, Tuple
from backend.sudoku_puzzle import SudokuPuzzle
from backend.user_data import UserData
from backend.authentication_manager import AuthenticationManager
from backend.service_manager import ServiceManager
from backend.sudoku_puzzle import HINT_COST, PUZZLE_SIZE
import backend.sudoku_generator as sudoku_generator


def generate_sudoku_puzzle(service_manager: ServiceManager, authentication_manager: AuthenticationManager, 
            token: str) -> MutableMapping[str, Any]:
    """
    Generates a sudoku puzzle.

    Precondition: isinstance(service_manager, ServiceManager) and
                  isinstance(authentication_manager, AuthenticationManager) and
                  isinstance(token, str)
    Postcondition: None

    Params - token: The specified authentication token.
    Return - The response to the client.
    """
    if not isinstance(service_manager, ServiceManager):
        raise Exception("service_manager must be a ServiceManager")
    if not isinstance(authentication_manager, AuthenticationManager):
        raise Exception("authentication_manager must be a AuthenticationManager")
    if not isinstance(token, str):
        raise TypeError("token must be a str")
    
    username: str = authentication_manager.get_username_for_token(token)
    if username is None:
        return {
            "success_code": 14,
            "error_message": f"Invalid authentication token"
        }

    user_data: Optional[UserData] = service_manager.get_data_for_user(username)

    if user_data is None:
        return {
            "success_code": 14,
            "error_message": f"Invalid authentication token"
        }

    sudoku_puzzle: SudokuPuzzle = sudoku_generator.generate_sudoku_puzzle()
    user_data.sudoku_puzzle = sudoku_puzzle

    return {
        "success_code": 0,
        "sudoku_puzzle": {
            "numbers": user_data.sudoku_puzzle.numbers,
            "number_locks": user_data.sudoku_puzzle.number_locks,
        }
    }

def update_sudoku_puzzle(service_manager: ServiceManager, authentication_manager: AuthenticationManager, 
            token: str, numbers: List[List[int]]):
    """
    Updates the sudoku puzzle.

    Precondition: isinstance(service_manager, ServiceManager) and
                  isinstance(authentication_manager, AuthenticationManager) and
                  isinstance(token, str) and
                  isinstance(numbers, list)
    Postcondition: None

    Params - token: The specified authentication token.
                numbers: The numbers to update the puzzle with.
    Return - The response to the client.
    """
    if not isinstance(service_manager, ServiceManager):
        raise Exception("service_manager must be a ServiceManager")
    if not isinstance(authentication_manager, AuthenticationManager):
        raise Exception("authentication_manager must be a AuthenticationManager")
    if not isinstance(token, str):
        raise Exception("token must be a str")
    if not isinstance(numbers, list):
        raise Exception("numbers must be a list")
    
    username: str = authentication_manager.get_username_for_token(token)
    if username is None:
        return {
            "success_code": 14,
            "error_message": "Invalid authentication token"
        }

    if len(numbers) != PUZZLE_SIZE:
        return {
            "success_code": 64,
            "error_message": "Invalid puzzle size"
        }
    for num_row in numbers:
        if len(num_row) != PUZZLE_SIZE:
            return {
                "success_code": 64,
                "error_message": "Invalid puzzle size"
            }

    user_data: Optional[UserData] = service_manager.get_data_for_user(username)

    if user_data is None:
        return {
            "success_code": 14,
            "error_message": "Invalid authentication token"
        }

    if user_data.sudoku_puzzle is None:
        return {
            "success_code": 61,
            "error_message": "No puzzle in progress"
        }

    puzzle: SudokuPuzzle = user_data.sudoku_puzzle

    coords = [(row, col) for row in range(PUZZLE_SIZE) for col in range(PUZZLE_SIZE)]

    for row, col in coords:
        cur_number = numbers[row][col]
        cur_colution = puzzle.solution[row][col]
        if cur_number not in range(PUZZLE_SIZE + 1):
            return {
                "success_code": 60,
                "error_message": f"Invalid number ({row}, {col})"
            }
        if puzzle.is_number_locked_at(row, col) and cur_number != cur_colution:
                return {
                    "success_code": 62,
                    "error_message": f"Can't change locked number ({row}, {col})"
                }
    
    for row, col in coords:
        puzzle.set_number_at(row, col, numbers[row][col])
    
    return {
        "success_code": 0,
    }

def buy_hint(service_manager: ServiceManager, authentication_manager: AuthenticationManager, 
            token: str) -> MutableMapping[str, Any]:
    """
    Buys a hint.

    Precondition: isinstance(service_manager, ServiceManager) and
                  isinstance(authentication_manager, AuthenticationManager) and
                  isinstance(token, str)
    Postcondition: None

    Params - token: The specified authentication token.
    Return - The response to the client.
    """
    if not isinstance(service_manager, ServiceManager):
        raise Exception("service_manager must be a ServiceManager")
    if not isinstance(authentication_manager, AuthenticationManager):
        raise Exception("authentication_manager must be a AuthenticationManager")
    if not isinstance(token, str):
        raise Exception("token must be a str")
    
    username: str = authentication_manager.get_username_for_token(token)
    if username is None:
        return {
            "success_code": 14,
            "error_message": f"Invalid authentication token"
        }

    user_data: Optional[UserData] = service_manager.get_data_for_user(username)

    if user_data is None:
        return {
            "success_code": 14,
            "error_message": f"Invalid authentication token"
        }

    if user_data.coins < HINT_COST:
        return {
            "success_code": 70,
            "error_message": f"Not enough coins (have {user_data.coins}, need {HINT_COST})"
        }

    sudoku_puzzle: Optional[SudokuPuzzle] = user_data.sudoku_puzzle

    if sudoku_puzzle is None:
        return {
            "success_code": 61,
            "error_message": f"No puzzle in progress"
        }
    
    hint_coords: Optional[Tuple[int, int]] = sudoku_puzzle.unlock_random_hint()
    if hint_coords is None:
        return {
            "success_code": 63,
            "error_message": "No valid cells for hint"
        }
    row: int = hint_coords[0]
    col: int = hint_coords[1]

    user_data.coins -= HINT_COST
    return {
        "success_code": 0,
        "number": sudoku_puzzle.get_number_at(row, col),
        "row": row,
        "col": col,
        "coins": user_data.coins,
    }

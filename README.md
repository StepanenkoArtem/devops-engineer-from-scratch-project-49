### Hexlet tests and linter status:
[![Actions Status](https://github.com/StepanenkoArtem/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/StepanenkoArtem/devops-engineer-from-scratch-project-49/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=StepanenkoArtem_devops-engineer-from-scratch-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=StepanenkoArtem_devops-engineer-from-scratch-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=StepanenkoArtem_devops-engineer-from-scratch-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=StepanenkoArtem_devops-engineer-from-scratch-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=StepanenkoArtem_devops-engineer-from-scratch-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=StepanenkoArtem_devops-engineer-from-scratch-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=StepanenkoArtem_devops-engineer-from-scratch-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=StepanenkoArtem_devops-engineer-from-scratch-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=StepanenkoArtem_devops-engineer-from-scratch-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=StepanenkoArtem_devops-engineer-from-scratch-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=StepanenkoArtem_devops-engineer-from-scratch-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=StepanenkoArtem_devops-engineer-from-scratch-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=StepanenkoArtem_devops-engineer-from-scratch-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=StepanenkoArtem_devops-engineer-from-scratch-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=StepanenkoArtem_devops-engineer-from-scratch-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=StepanenkoArtem_devops-engineer-from-scratch-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=StepanenkoArtem_devops-engineer-from-scratch-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=StepanenkoArtem_devops-engineer-from-scratch-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=StepanenkoArtem_devops-engineer-from-scratch-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=StepanenkoArtem_devops-engineer-from-scratch-project-49)

# Brain Games

A collection of simple console games to train your brain! This package includes five different mathematical and logical games:

## Games Description

1. **brain-even** - Determine if a given number is even
2. **brain-calc** - Calculate simple mathematical expressions  
3. **brain-gcd** - Find the greatest common divisor of two numbers
4. **brain-progression** - Find the missing number in an arithmetic progression
5. **brain-prime** - Determine if a given number is prime

## System Requirements

- Python 3.13 or higher
- uv package manager

## Installation

### Local installation for development:
```bash
git clone https://github.com/StepanenkoArtem/devops-engineer-from-scratch-project-49.git
cd devops-engineer-from-scratch-project-49
uv install
```

### Global installation:
```bash
uv tool install git+https://github.com/StepanenkoArtem/devops-engineer-from-scratch-project-49.git
```

## Usage

After installation, you can run any of the games by typing their names in the terminal:

```bash
brain-games    # Welcome message
brain-even     # Even number game
brain-calc     # Calculator game  
brain-gcd      # Greatest common divisor game
brain-progression  # Arithmetic progression game
brain-prime    # Prime number game
```

## Game Rules

Each game follows the same pattern:
- Answer 3 questions correctly to win
- One wrong answer ends the game
- Enter your answers when prompted

Good luck and have fun training your brain!

## Game Demonstrations

### brain-even
Determine if a given number is even.

**Winning game:**
![brain-even win](asciinemas/brain-even-win.gif)

**Losing game:**
![brain-even lose](asciinemas/brain-even-lose.gif)

### brain-calc
Calculate simple mathematical expressions.

**Winning game:**
![brain-calc win](asciinemas/brain-calc-win.gif)

**Losing game:**
![brain-calc lose](asciinemas/brain-calc-lose.gif)

### brain-gcd
Find the greatest common divisor of two numbers.

**Winning game:**
![brain-gcd win](asciinemas/brain-gcd-win.gif)

**Losing game:**
![brain-gcd lose](asciinemas/brain-gcd-lose.gif)

### brain-progression
Find the missing number in an arithmetic progression.

**Winning game:**
![brain-progression win](asciinemas/brain-progression-win.gif)

**Losing game:**
![brain-progression lose](asciinemas/brain-progression-lose.gif)

### brain-prime
Determine if a given number is prime.

**Winning game:**
![brain-prime win](asciinemas/brain-prime-win.gif)

**Losing game:**
![brain-prime lose](asciinemas/brain-prime-lose.gif)

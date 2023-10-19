#!/bin/bash

BASE_DIR="healthy_eats_reservation_app"

declare -a DIRS=(
    "$BASE_DIR/src/auth"
    "$BASE_DIR/src/restaurants"
    "$BASE_DIR/src/users"
    "$BASE_DIR/src/reservations"
    "$BASE_DIR/src/reviews"
    "$BASE_DIR/src/templates"
    "$BASE_DIR/migrations"
)

declare -a FILES=(
    "$BASE_DIR/src/__init__.py"
    "$BASE_DIR/src/auth/__init__.py"
    "$BASE_DIR/src/auth/routes.py"
    "$BASE_DIR/src/auth/forms.py"
    "$BASE_DIR/src/restaurants/__init__.py"
    "$BASE_DIR/src/restaurants/routes.py"
    "$BASE_DIR/src/restaurants/models.py"
    "$BASE_DIR/src/restaurants/services.py"
    "$BASE_DIR/src/users/__init__.py"
    "$BASE_DIR/src/users/routes.py"
    "$BASE_DIR/src/users/models.py"
    "$BASE_DIR/src/users/services.py"
    "$BASE_DIR/src/reservations/__init__.py"
    "$BASE_DIR/src/reservations/routes.py"
    "$BASE_DIR/src/reservations/models.py"
    "$BASE_DIR/src/reservations/services.py"
    "$BASE_DIR/src/reviews/__init__.py"
    "$BASE_DIR/src/reviews/routes.py"
    "$BASE_DIR/src/reviews/models.py"
    "$BASE_DIR/src/reviews/services.py"
    "$BASE_DIR/config.py"
    "$BASE_DIR/run.py"
)

for dir in "${DIRS[@]}"; do
    mkdir -p $dir
done

for file in "${FILES[@]}"; do
    touch $file
done

echo "Structure created successfully!"

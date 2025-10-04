"""This script adds a new crossword to the website"""

from datetime import datetime


i_frame = input("Please Enter the Iframe obtained from crosshare> ")
num = input("please enter the crossword number > ")
setter = input("please enter the setter > ")
standard_html = """
<html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
        <style>
            .custom-btn {
                background-color: #578295;
                border-color: #578295;
                color: white;
            }
            .custom-btn:hover {
                background-color: #466a7a;
                border-color: #466a7a;
                color: white;
            }
        </style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #578295;">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">
                    <img src="logo.jpg" alt="Logo" height="60">
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="archive/current">Current</a>
                        </li>
                        
                    </ul>
                </div>
            </div>
        </nav>
        
        {{CROSSWORD}}
    </body>
</html>
"""

card = f"""
        <div class="container mt-4">
            <div class="card mb-3" style="max-width: 540px;">
                <div class="row g-0">
                    <div class="col-md-3">
                        <img src="crossword.jpg" class="img-fluid rounded-start" alt="Crossword" style="object-fit: cover; height: 100%;">
                    </div>
                    <div class="col-md-9">
                        <div class="card-body">
                            <h5 class="card-title">Pelican {num}</h5>
                            <p class="card-text">{setter} - {datetime.today().strftime("%d/%m/%Y")}</p>
                            <a href="archive/{num}.html" class="btn custom-btn">Play</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
"""


# Write the individual crossword page
with open(rf"C:\Users\Michael\thepelicancrossing\archive\{num}.html", "w") as f:
    f.write(standard_html.replace("{{CROSSWORD}}", i_frame))

# Update the index.html by inserting the new card
index_path = r"C:\Users\Michael\thepelicancrossing\index.html"

# Read the existing index.html
with open(index_path, "r") as f:
    content = f.read()

# Find the position right after </nav> and insert the card there
nav_end = "</nav>"
nav_pos = content.find(nav_end)

if nav_pos != -1:
    # Insert the card right after the closing </nav> tag
    insert_pos = nav_pos + len(nav_end)
    new_content = content[:insert_pos] + "\n" + card + content[insert_pos:]

    # Write the updated content back
    with open(index_path, "w") as f:
        f.write(new_content)

    print(f"Successfully added Pelican {num} to the website!")
else:
    print("Error: Could not find </nav> tag in index.html")

"""This script adds a new crossword to the website"""

from datetime import datetime


i_frame = input("Please Enter the Iframe obtained from crosshare> ")
num = input("please enter the crossword number > ")
setter = input("please enter the setter > ")
standard_html = """
<html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
        <style>
            .custom-btn {
                background-color: #578295;
                border-color: #578295;
                color: white;
            }
            .custom-btn:hover {
                background-color: #466a7a;
                border-color: #466a7a;
                color: white;
            }
        </style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #578295;">
            <div class="container-fluid">
                <a class="navbar-brand" href="../">
                    <img src="logo.jpg" alt="Logo" height="60">
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="current">Current</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Archive</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        
        {{CROSSWORD}}
    </body>
</html>
"""

card = f"""
        <div class="container mt-4">
            <div class="card mb-3" style="max-width: 540px;">
                <div class="row g-0">
                    <div class="col-md-3">
                        <img src="crossword.jpg" class="img-fluid rounded-start" alt="Crossword" style="object-fit: cover; height: 100%;">
                    </div>
                    <div class="col-md-9">
                        <div class="card-body">
                            <h5 class="card-title">Pelican {num}</h5>
                            <p class="card-text">{setter} - {datetime.today().strftime("%d/%m/%Y")}</p>
                            <a href="archive/{num}.html" class="btn custom-btn">Play</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
"""

# Write the individual crossword page
with open(rf"C:\Users\Michael\thepelicancrossing\archive\{num}.html", "w") as f:
    f.write(standard_html.replace("{{CROSSWORD}}", i_frame))

# Update the index.html by inserting the new card
index_path = r"C:\Users\Michael\thepelicancrossing\index.html"

# Read the existing index.html
with open(index_path, "r") as f:
    content = f.read()

# Find the position right after </nav> and insert the card there
nav_end = "</nav>"
nav_pos = content.find(nav_end)

if nav_pos != -1:
    # Insert the card right after the closing </nav> tag
    insert_pos = nav_pos + len(nav_end)
    new_content = content[:insert_pos] + "\n" + card + content[insert_pos:]

    # Write the updated content back
    with open(index_path, "w") as f:
        f.write(new_content)

    print(f"Successfully added Pelican {num} to the website!")
else:
    print("Error: Could not find </nav> tag in index.html")

# Update the current crossword page
current_path = r"C:\Users\Michael\thepelicancrossing\current.html"

# Read the existing current.html
with open(current_path, "r") as f:
    current_content = f.read()

# Find the position right after </nav> and replace everything after it with the iframe
nav_end = "</nav>"
nav_pos = current_content.find(nav_end)

if nav_pos != -1:
    # Keep everything up to and including </nav>, then add the iframe and closing tags
    insert_pos = nav_pos + len(nav_end)
    new_current = (
        current_content[:insert_pos] + "\n        " + i_frame + "\n    </body>\n</html>"
    )

    # Write the updated content back
    with open(current_path, "w") as f:
        f.write(new_current)

    print(f"Successfully updated current crossword page with Pelican {num}!")
else:
    print("Error: Could not find </nav> tag in current.html")

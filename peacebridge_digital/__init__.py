<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Donate via M-Pesa</title>
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>

<body class="bg-light">

<div class="container mt-5 p-5 bg-white shadow rounded">
    <h2 class="text-center text-success">Support Our Project</h2>
    <p class="text-center">Enter your phone number and amount to donate via M-Pesa.</p>

    <form method="POST">
        {% csrf_token %}
        <div class="mb-3">
            <label class="form-label">Phone Number (2547xxxxx)</label>
            <input type="text" name="phone" class="form-control" required />
        </div>

        <div class="mb-3">
            <label class="form-label">Amount</label>
            <input type="number" name="amount" class="form-control" required />
        </div>

        <button class="btn btn-success w-100">Donate</button>
    </form>
</div>

</body>
</html>
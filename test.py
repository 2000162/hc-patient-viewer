import libsql_client

def deletePerson(name):
    with libsql_client.create_client_sync(
        "libsql://patientdata-heyingz.turso.io",
        auth_token="eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3MzEyNTY3NzEsImlkIjoiMzg0YTcxYzQtODA3OS00NDYyLWI3MzktZDNmZWUxOGU4MzAzIn0.Dy6ULddDvLPfHKi77E9L85IfAZ-svnGynCXLQRlDuH4hSABwT7ixlNYfxE02jn35yHp3L1FZC9D4L64KpxpiCg"
    ) as client:
        command = "DELETE FROM Patient WHERE first_name = \"" + name +"\""
        result = client.execute(command)

def addPerson(id, f_name, l_name):
    with libsql_client.create_client_sync(
        "libsql://patientdata-heyingz.turso.io",
        auth_token="eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3MzEyNTY3NzEsImlkIjoiMzg0YTcxYzQtODA3OS00NDYyLWI3MzktZDNmZWUxOGU4MzAzIn0.Dy6ULddDvLPfHKi77E9L85IfAZ-svnGynCXLQRlDuH4hSABwT7ixlNYfxE02jn35yHp3L1FZC9D4L64KpxpiCg"
    ) as client:
        command = "INSERT INTO Patient (patient_id, first_name, last_name) VALUES (1234, 'Pranav', 'Sreepada');"
        result = client.execute(command)

addPerson(1234, "Pranav", "Sreepada")

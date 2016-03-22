import iupc
import jwxt

if __name__ == "__main__":
    iupc_worker = iupc.Iupc()
    iupc_worker.login()

    jwxt_worker = jwxt.Jwxt(iupc_worker.session)

    response = jwxt_worker.auth()
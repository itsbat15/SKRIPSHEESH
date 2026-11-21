const key = "artha_access_token";
export const workspaceChanged = "artha:workspace-changed";

export const homeFor = (role) => role === "super_admin" ? "/dashboard/superadmin" : "/dashboard/frontdesk";
export const accessToken = () => sessionStorage.getItem(key);
export function storeToken(token) {
  if (token) sessionStorage.setItem(key,token);
  else sessionStorage.removeItem(key);
}

export async function arthaFetch(path,options={}) {
  const headers = new Headers(options.headers);
  headers.set("Accept","application/json");
  const token = accessToken();
  if (token) headers.set("Authorization",`Bearer ${token}`);
  const direct = process.env.NEXT_PUBLIC_ARTHA_API_URL?.replace(/\/$/,"") || "";
  const response = await fetch(`${direct}/api/artha/${path}`,{
    ...options,headers,cache:"no-store",credentials:"omit",
  });
  if (!response.ok) {
    const result = await response.json().catch(()=>({}));
    const error = new Error(result.message || "Permintaan tidak berhasil. Coba kembali.");
    error.status = response.status;
    if (error.status === 401 && path !== "login") storeToken(null);
    throw error;
  }
  return response;
}

export const readArtha = async (path, options) => (await arthaFetch(path,options)).json();

export function writeArtha(action, form) {
  const id = form.get("id");
  const routes = {
    login:["login"],logout:["logout"],register:["enrollments"],pay:[`bills/${id}/payments`],
    "save-group":[id ? `study-groups/${id}` : "study-groups",Boolean(id)],
    "save-student":[`students/${id}`,true],
    "save-branch":[id ? `branches/${id}` : "branches",Boolean(id)],
    "save-user":[id ? `staff/${id}` : "staff",Boolean(id)],
    "save-package":[id ? `course-packages/${id}` : "course-packages",Boolean(id)],
    "review-payment":[`payments/${id}/review`,true],
    "close-day":["reconciliations"],"approve-close":[`reconciliations/${id}/approval`,true],
  };
  const [path,patch] = routes[action];
  return readArtha(path,patch ?
    {method:"PATCH",headers:{"Content-Type":"application/json"},body:JSON.stringify(Object.fromEntries(form))} :
    {method:"POST",body:form});
}

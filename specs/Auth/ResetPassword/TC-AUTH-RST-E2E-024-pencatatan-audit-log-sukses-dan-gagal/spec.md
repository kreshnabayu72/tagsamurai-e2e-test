---
id: TC-AUTH-RST-E2E-024-pencatatan-audit-log-sukses-dan-gagal
title: "Pencatatan audit log di dua surface (Activity Log > Session dan User Log): event sukses, event gagal, dan atribut entri"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-94
  - TC-AUTH-RST-95
  - TC-AUTH-RST-96
  - TC-AUTH-RST-97
  - TC-AUTH-RST-98
  - TC-AUTH-RST-99
  - TC-AUTH-RST-100
  - TC-AUTH-RST-101
  - TC-AUTH-RST-102
  - TC-AUTH-RST-103
  - TC-AUTH-RST-134
  - TC-AUTH-RST-135
  - TC-AUTH-RST-136
coverage:
  web: automated
---

# Pencatatan audit log di dua surface (Activity Log > Session dan User Log): event sukses, event gagal, dan atribut entri

## Prerequisites

- User belum login (guest); alur Reset Password dijalankan di browser web.
- Admin `superAdminGlobalSettings_automated_qaTeam1@qwertysystem.net` (Role: Total Control) memiliki akses ke:
  1. Global Settings > Activity Log > Session.
  2. Global Settings > User > Detail User > tab User Log.

## Test Steps

### Pencatatan event sukses Request Reset Password

1. Lakukan request reset sukses untuk user `budisantoso@qwertysystem.net`
2. Buka Global Settings > Activity Log > Session lalu filter Activity = "Reset Password"
3. Buka Global Settings > User > Detail "Budi Santoso" > tab User Log
4. Verifikasi pada kedua surface muncul entri baru dengan:
   - Activity: "Reset Password"
   - Status: "Success"
   - Note: "Password reset requested"

### Pencatatan event gagal Request pada akun Inactive

5. Lakukan request reset untuk user `tonokurniawan@qwertysystem.net` (Inactive)
6. Periksa Activity Log Session dan User Log Tono Kurniawan
7. Verifikasi tercatat entri:
   - Activity: "Reset Password"
   - Status: "Failed"
   - Note: "Account is inactive"

### Pencatatan event gagal kuota 5 kali per email (Request dan Resend)

8. Lakukan request reset ke-6 (melebihi kuota 5x) untuk user `fajarnugroho@qwertysystem.net`
9. Periksa Activity Log Session dan User Log
10. Verifikasi tercatat entri: Status "Failed", Note "Too many reset attempts"
11. Lakukan resend ke-6 (melebihi kuota) untuk user lain
12. Verifikasi tercatat entri: Status "Failed", Note "Too many reset attempts"

### Pencatatan event gagal Submit pelanggaran Password Policy

13. Pada form Setup New Password, lakukan submit password yang melanggar policy (misal: tanpa angka/simbol)
14. Periksa Activity Log Session dan User Log
15. Verifikasi tercatat entri: Status "Failed", Note "Password does not meet requirements"

### Pencatatan event gagal Submit password sama dengan password lama

16. Lakukan submit password baru yang sama dengan password aktif saat ini
17. Periksa Activity Log Session dan User Log
18. Verifikasi tercatat entri: Status "Failed", Note "Password does not meet requirements"

### Pencatatan event sukses Submit New Password

19. Lakukan submit password baru yang valid hingga mendarat di Password Reset Successful
20. Periksa Activity Log Session dan User Log
21. Verifikasi tercatat entri:
    - Activity: "Reset Password"
    - Status: "Success"
    - Note: "Password updated successfully"

### Pencatatan token expired, consumed, dan invalidated saat Submit

22. Lakukan submit menggunakan token yang sudah expired (>24 jam)
23. Verifikasi tercatat entri: Status "Failed", Note "Reset link expired"
24. Lakukan submit menggunakan token yang sudah consumed (dari tab lain)
25. Verifikasi tercatat entri: Status "Failed", Note "Reset link already used"
26. Lakukan submit menggunakan token yang sudah di-invalidate oleh Resend
27. Verifikasi tercatat entri: Status "Failed", Note "Reset link expired"
28. Lakukan submit atau validasi link saat akun berstatus deleted/inactive
29. Verifikasi tercatat entri: Status "Failed", Note "Reset link expired"

### Validasi atribut entri log dan ketahanan penulisan (Atomicity)

30. Periksa kolom-kolom pada baris log yang tercatat
31. Verifikasi kolom IP Address terisi alamat IP publik pemanggil yang valid
32. Verifikasi kolom Device / Browser terisi dengan format kanonikal: `[Browser] on [OS]` (misal: `Chrome on Windows`)
33. Simulasikan kegagalan penulisan audit log ke database (fault injection) saat eksekusi submit
34. Verifikasi kegagalan penulisan log membatalkan seluruh aksi pembaruan password (transaksi atomik)

## Notes

- Sesuai PRD §8, §9.2 F-AUTHRST-05, §9.8, dan keputusan NC-18, audit log untuk seluruh kejadian Reset Password disinkronkan secara konsisten ke dua permukaan (surface): Activity Log > Session (level tenant) dan User Log (level akun individual).
- Sesuai keputusan NC-19, penulisan log bersifat atomik dengan keputusan aksi sehingga kegagalan pencatatan log akan membatalkan aksi pembaruan password.

---
id: TC-AUTH-RST-E2E-011-penolakan-resend-email
title: "Penolakan Resend Email: akun nonaktif, akun dihapus, kuota per email habis, dan budget bersama"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-33
  - TC-AUTH-RST-47
  - TC-AUTH-RST-48
  - TC-AUTH-RST-49
coverage:
  web: automated
---

# Penolakan Resend Email: akun nonaktif, akun dihapus, kuota per email habis, dan budget bersama

## Prerequisites

- User belum login (guest); telah berhasil melakukan request reset awal dan berada di halaman Email Sent!.
- Admin pemantau log `superAdminGlobalSettings_automated_qaTeam1@qwertysystem.net` dapat mengubah status akun dan memantau log.
- Mail-catcher siap memantau ada atau tidaknya email baru.

## Test Steps

### Resend untuk akun yang menjadi Inactive setelah Request

1. Buka halaman Email Sent! untuk user `tonokurniawan@qwertysystem.net`
2. Melalui sesi admin di Global Settings > User, ubah status akun Tono Kurniawan menjadi Inactive
3. Tunggu cooldown 60 detik selesai lalu klik tombol [Resend email]
4. Verifikasi UI tetap menampilkan toast sukses "Success, email has been sent to tonokurniawan@qwertysystem.net." untuk mencegah enumerasi
5. Verifikasi pada mail-catcher tidak ada email baru yang masuk
6. Verifikasi tidak ada token baru yang diterbitkan di database
7. Buka Activity Log Session dan User Log menggunakan sesi admin
8. Verifikasi tercatat entri log baru dengan Activity "Reset Password", Status "Failed", dan Note "Account is inactive"

### Resend untuk akun yang dihapus (Deleted) setelah Request

9. Siapkan halaman Email Sent! untuk user uji sementara
10. Melalui sesi admin di Global Settings > User, hapus akun uji tersebut
11. Tunggu cooldown 60 detik selesai lalu klik tombol [Resend email]
12. Verifikasi UI tetap menampilkan toast sukses semu
13. Verifikasi tidak ada email baru dan tidak ada token baru yang diterbitkan
14. Verifikasi tidak ada entri baru yang dicatat di log (zero-logging untuk akun deleted)

### Pembagian budget 5 kali antara Request dan Resend

15. Siapkan akun `dewilestari@qwertysystem.net` dengan kombinasi 3 kali Request dan 2 kali Resend dalam rentang 24 jam (total 5 aksi)
16. Verifikasi aksi ke-5 (Resend ke-2) masih berhasil mengirimkan email dan token
17. Verifikasi Request dan Resend berbagi satu kuota gabungan 5 kali per 24 jam untuk email yang sama

### Resend melebihi batas 5 kali per email

18. Pada halaman Email Sent! milik akun yang telah mencapai total 5 aksi dalam 24 jam, tunggu cooldown selesai
19. Klik tombol [Resend email] untuk aksi ke-6
20. Verifikasi UI tetap menampilkan toast sukses semu: "Success, email has been sent to dewilestari@qwertysystem.net."
21. Verifikasi pada mail-catcher tidak ada email baru yang dikirimkan
22. Buka Activity Log Session dan User Log menggunakan sesi admin
23. Verifikasi tercatat entri log baru dengan Activity "Reset Password", Status "Failed", dan Note "Too many reset attempts"

## Notes

- Sesuai keputusan NC-06 dan PRD §9.4.2 baris 16-19, sistem menjaga respons UI tetap seragam (toast sukses) pada skenario akun Inactive, Deleted, maupun limit per email untuk mencegah peretas mengetahui kondisi akun melalui tombol Resend.
- Event kegagalan internal dicatat secara presisi pada audit log (Failed / "Account is inactive" atau Failed / "Too many reset attempts").

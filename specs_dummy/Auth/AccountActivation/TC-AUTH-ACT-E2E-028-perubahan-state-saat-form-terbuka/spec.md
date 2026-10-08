---
id: TC-AUTH-ACT-E2E-028-perubahan-state-saat-form-terbuka
title: "Perubahan state saat form terbuka: Resend, kedaluwarsa, status berubah, dan password sudah ada"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-ACT-123
  - TC-AUTH-ACT-124
  - TC-AUTH-ACT-129
  - TC-AUTH-ACT-130
coverage:
  web: automated
---

# Perubahan state saat form terbuka: Resend, kedaluwarsa, status berubah, dan password sudah ada

## Prerequisites

- Browser publik tanpa sesi login (jendela privat) untuk alur aktivasi.
- Sesi login Role: Total Control (Global Settings) di browser admin, untuk klik Resend Activation Email.
- Akses mailbox uji (mail catcher atau inbox riil) untuk memverifikasi token baru setelah Resend.
- `Mode: mock` — fixture BE untuk: (a) token yang di-set berusia 23 jam 59 menit lalu digeser lewat 24 jam pada TC-AUTH-ACT-124, (b) user berstatus Activated tanpa mengonsumsi token (TC-AUTH-ACT-129), (c) user dengan kredensial yang sudah berisi password (TC-AUTH-ACT-130); ditambah kemampuan mengirim request Set Password langsung ke server.
- 4 user seeding milik automation, dibuat lewat API di hook `before` (email unik per run), satu user untuk tiap blok TC-AUTH-ACT-123, 124, 129, dan 130; hook `after` membersihkan seluruh user.
- Akses API read-only untuk memverifikasi status token dan password sebelum serta sesudah tiap submit.

## Test Steps

### Resend saat form terbuka: submit token lama diarahkan ke Invalid Link (TC-AUTH-ACT-123)

1. Buka link aktivasi user A → halaman `Auth > Account Activation > Set Password` tampil.
2. Ketik `Aman#Sandi8` pada field Password dan `Aman#Sandi8` pada field Confirm Password.
3. Pada browser admin, klik Resend Activation Email untuk user A di `Global Settings > User > Login User`.
4. Kembali ke tab form dan klik button "Set Password".
5. Verifikasi tab form diarahkan ke halaman Invalid Link varian Expired (Title "Activation Link Expired").
6. Verifikasi tidak ada set password yang tersimpan dan tidak ada toast.
7. Verifikasi via API bahwa token lama Superseded, token baru Active, dan status user tetap Pending Activation.

### Token kedaluwarsa saat form terbuka (TC-AUTH-ACT-124)

8. Buka link aktivasi user B (token berusia 23 jam 59 menit) → halaman Set Password tampil.
9. Ketik `Aman#Sandi8` pada kedua field.
10. Majukan waktu server uji sampai token berusia lebih dari 24 jam.
11. Klik button "Set Password".
12. Verifikasi tab form diarahkan ke halaman Invalid Link varian Expired (Title "Activation Link Expired").
13. Verifikasi tidak ada set password yang tersimpan dan tidak ada toast.
14. Verifikasi via API bahwa status user tetap Pending Activation.

### Status user bukan Pending walau token masih Active (TC-AUTH-ACT-129)

15. Buka link aktivasi user C (berstatus Activated tanpa mengonsumsi token).
16. Verifikasi halaman Invalid Link varian Expired tampil dan form Set Password tidak dirender.
17. Kirim request Set Password langsung ke server dengan token yang sama, Password dan Confirm Password `Aman#Sandi8`.
18. Verifikasi server menolak dengan 409 dan FE mengarahkan ke Invalid Link varian Expired.
19. Verifikasi via API bahwa password tidak berubah, status user tetap Activated, dan token tidak berubah.

### Password sudah ada walau token masih Active (TC-AUTH-ACT-130)

20. Kirim request Set Password langsung ke server dengan token user D, Password dan Confirm Password `Aman#Sandi8`.
21. Verifikasi server menolak dengan 409.
22. Verifikasi FE mengarahkan ke halaman Invalid Link varian Expired.
23. Verifikasi via API bahwa password yang sudah ada tidak berubah dan token tidak berubah menjadi Consumed oleh request ini.

## Notes

- Keempat kasus berbagi topik "state berubah setelah form valid terbuka, sehingga submit ditolak"; tidak ada aktivasi sukses sehingga urutan blok bebas.
- Kebutuhan Resend dengan cooldown berakhir, fixture waktu, dan fixture status/kredensial dicatat di Prerequisites sebagai bahan tim FE.

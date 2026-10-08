---
id: TC-AUTH-ACT-E2E-026-tampilan-respons-422-400
title: "Tampilan Set Password saat server menjawab 422 dengan field, 400 tanpa field, dan 400 tanpa token"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-117
  - TC-AUTH-ACT-118
  - TC-AUTH-ACT-132
coverage:
  web: automated
---

# Tampilan Set Password saat server menjawab 422 dengan field, 400 tanpa field, dan 400 tanpa token

## Prerequisites

- Browser publik tanpa sesi login.
- `Mode: mock` — kemampuan mengatur respons submit via intercept jaringan (422 dengan field `password`, 400 tanpa informasi field) dan mengirim request tanpa field token / dengan body bukan JSON yang valid.
- 2 user seeding milik automation berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run): user A untuk TC-AUTH-ACT-117 dan user B untuk TC-AUTH-ACT-118; TC-AUTH-ACT-132 memakai request tanpa token sehingga tidak memerlukan user; hook `after` membersihkan user.
- Akses API read-only untuk memverifikasi status respons dan token tetap Active.

## Test Steps

### Server menjawab 422 untuk request yang lolos validasi client (TC-AUTH-ACT-117)

1. Buka link aktivasi user A → halaman `Auth > Account Activation > Set Password` tampil.
2. Atur respons submit menjadi 422 dengan field `password` dan pesan dari server.
3. Ketik `Aman#Sandi8` pada field Password dan `Aman#Sandi8` pada field Confirm Password.
4. Klik button "Set Password".
5. Verifikasi inline error muncul di bawah field Password memakai pesan dari respons server.
6. Verifikasi halaman tetap di Set Password, nilai kedua field dipertahankan, dan tidak ada toast.
7. Verifikasi via API bahwa token user A tetap Active dan status user tetap Pending Activation.

### Server menjawab 400 tanpa informasi field (TC-AUTH-ACT-118)

8. Buka link aktivasi user B → halaman Set Password tampil.
9. Atur respons submit menjadi 400 tanpa informasi field.
10. Ketik `Aman#Sandi8` pada kedua field, lalu klik button "Set Password".
11. Verifikasi dialog tampil memuat teks "Invalid request. Please check your input."
12. Verifikasi halaman tetap di Set Password di belakang dialog dengan nilai field dipertahankan, dan tidak ada toast.
13. Verifikasi via API bahwa token user B tetap Active dan status user tetap Pending Activation.

### Request tanpa token atau body salah bentuk ditolak 400 (TC-AUTH-ACT-132)

14. Kirim request Set Password langsung ke server tanpa field token, dengan Password dan Confirm Password `Aman#Sandi8`.
15. Kirim request kedua dengan body bukan JSON yang valid.
16. Verifikasi kedua request ditolak server dengan 400.
17. Atur respons submit form menjadi 400 tanpa informasi field, lalu isi kedua field dengan `Aman#Sandi8` dan klik button "Set Password".
18. Verifikasi halaman tetap di Set Password, nilai field dipertahankan, tanpa toast (state S-20).
19. Verifikasi tidak ada data yang berubah.

## Notes

- Ketiga TC berbagi topik yang sama (tampilan saat respons error non-5xx dari server) dan semuanya tidak mengonsumsi token sehingga urutan blok bebas.
- Kebutuhan mock respons dan request langsung dicatat di Prerequisites.

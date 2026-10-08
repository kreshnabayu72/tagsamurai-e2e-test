---
id: TC-AUTH-ACT-E2E-022-resend-admin-console-dan-bulk
title: "Resend Activation Email dari Admin Console dan Bulk Resend dari Global Settings > User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-100
  - TC-AUTH-ACT-101
coverage:
  web: automated
---

# Resend Activation Email dari Admin Console dan Bulk Resend dari Global Settings > User

## Prerequisites

- Sesi login Role: Total Control (Admin Console) untuk TC-AUTH-ACT-100.
- Sesi login Role: Total Control (Global Settings) untuk TC-AUTH-ACT-101.
- Jendela privat tanpa sesi login untuk membuka link aktivasi.
- Akses mailbox uji (mail catcher atau inbox riil) untuk mengambil link aktivasi lama dan baru tiap user.
- Kemampuan menunggu atau meng-mock cooldown Resend Activation Email.
- 3 user seeding milik automation berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run): user A (resend dari Admin Console), user B dan user C (bulk resend); hook `after` membersihkan seluruh user.
- Akses API read-only untuk memverifikasi status token (Active/Superseded) ketiga user.

## Test Steps

### Resend dari Admin Console membuat link lama invalid (TC-AUTH-ACT-100)

1. Ambil link aktivasi dari email pertama user A (link A).
2. Pada `Admin Console > Settings > User`, klik Resend Activation Email untuk user A.
3. Ambil link aktivasi dari email baru (link B).
4. Buka link A.
5. Verifikasi halaman Invalid Link varian Expired tampil untuk link A walau belum 24 jam.
6. Buka link B.
7. Verifikasi halaman Set Password tampil dengan Subtitle "Set a password to log in for <email user A>."
8. Verifikasi via API bahwa token A user tersebut Superseded dan token B Active.

### Bulk Resend membuat link lama kedua user invalid (TC-AUTH-ACT-101)

9. Ambil link aktivasi dari email pertama user B (link A1) dan user C (link A2).
10. Pada `Global Settings > User > Login User`, centang user B dan user C, buka Bulk Action, pilih Resend Activation Email.
11. Ambil link baru untuk masing-masing user (B1 dan B2).
12. Buka link A1, lalu link A2.
13. Verifikasi keduanya masing-masing menampilkan halaman Invalid Link varian Expired.
14. Buka link B1.
15. Verifikasi halaman Set Password tampil dengan Subtitle "Set a password to log in for <email user B>."
16. Buka link B2.
17. Verifikasi halaman Set Password tampil dengan Subtitle "Set a password to log in for <email user C>."
18. Verifikasi via API bahwa token lama kedua user Superseded dan token baru masing-masing Active.

## Notes

- Kedua blok memiliki aksi, dataset, dan tujuan berbeda (Admin Console tunggal vs Bulk Action di Global Settings) sehingga TC dipisah menjadi blok terpisah dalam satu spec.
- Tidak ada token yang dikonsumsi, sehingga urutan blok bebas; screening dilakukan pada blok pertama.
- Kebutuhan dua sesi role dan mailbox uji dicatat di Prerequisites.

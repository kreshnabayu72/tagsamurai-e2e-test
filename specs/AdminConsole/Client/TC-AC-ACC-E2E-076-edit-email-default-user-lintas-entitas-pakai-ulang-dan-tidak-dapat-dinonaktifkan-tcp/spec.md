---
id: TC-AC-ACC-E2E-076-edit-email-default-user-lintas-entitas-pakai-ulang-dan-tidak-dapat-dinonaktifkan-tcp
title: "Edit Email Default User: Email Lintas Entitas Diterima, Data Client Dihapus Dipakai Ulang, dan Default User Tidak Dapat Dinonaktifkan (Total Control)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-534
  - TC-AC-ACC-535
  - TC-AC-ACC-543
coverage:
  web: automated
---

# Edit Email Default User: Email Lintas Entitas Diterima, Data Client Dihapus Dipakai Ulang, dan Default User Tidak Dapat Dinonaktifkan (Total Control)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (A-01) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login akun Total Control Principal di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya. `{r6}` = 6 digit terakhir `{runId}` (dipakai agar Client Code tetap maksimal 15 karakter).
- Dataset seed (nama bersuffix): Client `PT Baru Daftar {runId}-076` (replika C-09: Direct, Group Cabang Menteng, tanpa subscription, Default User Not Yet Activated `hadi.prasetyo+{runId}-076@qwertysystem.net`; target TC-534); Client `PT Baru Daftar Dua {runId}-076` (replika yang sama, Client Code `BRD-{r6}`; target TC-535); Client `PT Dihapus Edit {runId}-076` (replika C-EDT-2: Client Code `DHE-{r6}`, Email Default User `dihapusedit+{runId}-076@qwertysystem.net`, sudah di-soft-delete); Client `PT Teknologi Maju {runId}-076` (replika C-02: Active, Partner CV Mitra Sejati sebagai Anchor dan CV Mitra Lestari, Group Area Jakarta, Client Code `TKM-{r6}`, Default User Not Yet Activated dengan Division seed `Finance` dan Position seed `Finance Manager`) (target TC-543). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Email akun untuk TC-534: A-13 `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net`, A-14 `totalControlPartner_automated_cvMitraSejati@qwertysystem.net`, A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`.
- Kemampuan teknis (TC-543): membuka Global Settings tenant Client > User dan menyorot (hover) Toggle Active serta row action Delete (cara masuk tidak dijelaskan TC; disediakan tim FE/BE).
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-534: Email sama dengan user Principal, Distributor, atau Partner diterima

1. Ketik Search `PT Baru Daftar {runId}-076`, tekan Enter
2. Buka `⋯` baris `PT Baru Daftar {runId}-076` lalu klik `Edit`
3. Ketik Email Default User `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net`, tunggu sekitar 500 ms
4. Verifikasi tidak ada pesan "Email already exists" untuk email A-13
5. Ketik Email Default User `totalControlPartner_automated_cvMitraSejati@qwertysystem.net`, tunggu sekitar 500 ms
6. Verifikasi tidak ada pesan "Email already exists" untuk email A-14
7. Ketik Email Default User `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, tunggu sekitar 500 ms
8. Verifikasi tidak ada pesan "Email already exists" untuk email A-01
9. Klik `[Save]`
10. Verifikasi popup tertutup
11. Verifikasi toast sukses "Success, client has been updated."

### TC-535: Company Name, Client Code, dan Email milik Client yang dihapus dipakai ulang

12. Ketik Search `PT Baru Daftar Dua {runId}-076`, tekan Enter
13. Buka `⋯` baris `PT Baru Daftar Dua {runId}-076` lalu klik `Edit`
14. Ubah Company Name menjadi `PT Dihapus Edit {runId}-076`
15. Ubah Client Code menjadi `DHE-{r6}`
16. Ubah Email Default User menjadi `dihapusedit+{runId}-076@qwertysystem.net`, tunggu sekitar 500 ms
17. Verifikasi tidak ada pesan "Company name already exists"
18. Verifikasi tidak ada pesan "Client code already exists"
19. Verifikasi tidak ada pesan "Email already exists"
20. Klik `[Save]`
21. Verifikasi popup tertutup
22. Verifikasi toast sukses "Success, client has been updated."
23. Ketik Search `PT Dihapus Edit {runId}-076`, tekan Enter
24. Klik Company Name `PT Dihapus Edit {runId}-076` untuk membuka Detail
25. Verifikasi Detail menampilkan Company Name "PT Dihapus Edit {runId}-076", Client Code "DHE-{r6}", dan Email Default User "dihapusedit+{runId}-076@qwertysystem.net"
26. Klik breadcrumb "Client" untuk kembali ke List

### TC-543: Default User tetap tidak dapat dinonaktifkan

27. Ketik Search `PT Teknologi Maju {runId}-076`, tekan Enter
28. Buka `⋯` baris `PT Teknologi Maju {runId}-076` lalu klik `Edit`
29. Ubah Last Name Default User menjadi `Pratama`
30. Klik `[Save]`
31. Verifikasi popup tertutup
32. Verifikasi toast sukses "Success, client has been updated."
33. Buka Global Settings > User tenant "PT Teknologi Maju {runId}-076"
34. Verifikasi nama Default User pada daftar user tenant memuat "Pratama"
35. Arahkan kursor ke Toggle Active baris Default User
36. Verifikasi Toggle Active baris Default User tampil dan berstatus disabled dengan tooltip "Default User cannot be modified."
37. Arahkan kursor ke row action Delete baris Default User
38. Verifikasi row action Delete baris Default User tampil dan berstatus disabled dengan tooltip "Default User cannot be modified."

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Langkah penghubung (S-03): Search nama unik, Detail, breadcrumb "Client".
- Alasan di atas 35 langkah (sekitar 38 langkah): satu role dan tiga Client seed milik sendiri; tiga blok (email lintas entitas, pakai ulang data dihapus, Default User tidak dapat dinonaktifkan) berdiri sendiri.
- Target tulis memakai Client seed milik spec; email akun aktor A-01, A-13, A-14 hanya dipakai sebagai nilai Email Default User (NC-03), tanpa mengubah akun Pre-setup.
- Temuan untuk QA:
  - TC-534 Post Condition ("kembalikan Email ... ke hadi.prasetyo") adalah pemulihan; cleanup menghapus Client seed.
  - TC-543 butir b ("Nama Default User ... memuat Pratama") tidak menyebut format nama di daftar user; spec memverifikasi substring.

---
id: TC-AC-ACC-E2E-077-edit-activation-email-ke-inbox-baru-tautan-lama-dan-term-pertama-tcp
title: "Edit Email Default User: Activation Email Baru ke Inbox, Tautan Lama Tidak Berlaku, dan Pengiriman Saat Term Pertama Aktif (Total Control)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-153
  - TC-AC-ACC-154
coverage:
  web: automated
---

# Edit Email Default User: Activation Email Baru ke Inbox, Tautan Lama Tidak Berlaku, dan Pengiriman Saat Term Pertama Aktif (Total Control)

## Prerequisites

- Mode: FE+BE. Kelas harness eksternal (mail-catcher) sebagai objek pembaca; tidak ada manipulasi jam.
- Akun aktor: Total Control Principal (A-01) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login akun Total Control Principal di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Dataset seed (nama bersuffix): Client `PT Aktivasi Tautan Lama {runId}-077` (replika C-FX11-1: Active, FAMS Grace, Default User Not Yet Activated dengan email awal `tautanlama.awal+{runId}-077@qwertysystem.net`, tautan aktivasi awal dari keluaran skrip seed); Client `PT Aktivasi Pertama {runId}-077` (replika C-EDT-1: Direct, Group Cabang Menteng, belum pernah memiliki subscription, Default User Not Yet Activated dengan email `mayaputri+{runId}-077@qwertysystem.net`). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Kemampuan teknis: mail-catcher dengan baseline jumlah email per alamat sebelum aksi (S-12, R-11); membuka tautan aktivasi awal; membaca Changelog, System Log (Settings > User > Detail akun aktor > Tab System Log), dan Activity Log Admin Console dengan Search nama unik (baseline nol); mengaktifkan term pertama FAMS dari License Allocation > Client Subscription (cara detail tidak dijelaskan TC; disediakan tim FE/BE).
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-153: Email diubah, ada subscription aktif

1. Catat baseline jumlah email di mail-catcher untuk `admin.baru+{runId}-077@qwertysystem.net`
2. Ketik Search `PT Aktivasi Tautan Lama {runId}-077`, tekan Enter
3. Buka `⋯` baris `PT Aktivasi Tautan Lama {runId}-077` lalu klik `Edit`
4. Ubah Email Default User menjadi `admin.baru+{runId}-077@qwertysystem.net`
5. Klik `[Save]`
6. Verifikasi toast sukses edit "Success, client has been updated."
7. Verifikasi toast sukses "Success, activation email has been sent." tampil sesudah toast sukses edit
8. Buka tautan aktivasi awal Default User dari keluaran skrip seed
9. Verifikasi tautan aktivasi awal tidak dapat dipakai untuk aktivasi
10. Buka inbox `admin.baru+{runId}-077@qwertysystem.net`
11. Verifikasi inbox menerima Activation Email (jumlah email naik satu dari baseline)
12. Kembali ke Admin Console > Client
13. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Aktivasi Tautan Lama {runId}-077`, tekan Enter
14. Verifikasi dua baris teratas (Date terbaru, bertanggal hari ini, urutan bebas) ber-Client Name "PT Aktivasi Tautan Lama {runId}-077" dan Modified By aktor: Action `Edit`, Field `Default User Email`, Old Value `tautanlama.awal+{runId}-077@qwertysystem.net`, New Value `admin.baru+{runId}-077@qwertysystem.net`; Action `Resend Activation Email`, Field `Email`, Old Value `—`, New Value `admin.baru+{runId}-077@qwertysystem.net`
15. Buka Settings > User > Detail akun aktor > Tab System Log, cari `PT Aktivasi Tautan Lama {runId}-077`
16. Verifikasi System Log: dua baris teratas dengan Object `Client`, Name "PT Aktivasi Tautan Lama {runId}-077": Action `Edit` (Field `Default User Email`, Old Value `tautanlama.awal+{runId}-077@qwertysystem.net`, New Value `admin.baru+{runId}-077@qwertysystem.net`) dan Action `Resend Activation Email` (Field `Email`, Old Value `—`, New Value `admin.baru+{runId}-077@qwertysystem.net`)
17. Buka Activity Log Admin Console (Tab User Action), saring Object "Client", cari `PT Aktivasi Tautan Lama {runId}-077`
18. Verifikasi Activity Log: dua baris teratas yang sama dengan System Log, Modified By aktor

### TC-154: Email diubah, belum ada subscription aktif

19. Catat baseline jumlah email di mail-catcher untuk `mayaputri+{runId}-077@qwertysystem.net` (lama) dan `mayaputri.baru+{runId}-077@qwertysystem.net` (baru)
20. Buka Admin Console > Client
21. Ketik Search `PT Aktivasi Pertama {runId}-077`, tekan Enter
22. Buka `⋯` baris `PT Aktivasi Pertama {runId}-077` lalu klik `Edit`
23. Ubah Email Default User menjadi `mayaputri.baru+{runId}-077@qwertysystem.net`
24. Klik `[Save]`
25. Verifikasi popup tertutup
26. Verifikasi toast sukses "Success, client has been updated."
27. Verifikasi tidak ada Activation Email baru di inbox email lama maupun email baru (jumlah email tetap sama dengan baseline)
28. Aktifkan term pertama FAMS "PT Aktivasi Pertama {runId}-077" dari License Allocation > Client Subscription
29. Verifikasi Activation Email diterima di inbox email baru (jumlah email naik satu dari baseline)
30. Verifikasi tidak ada Activation Email baru di inbox email lama

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Langkah penghubung (S-03): baseline email, Search nama unik, kembali ke Admin Console > Client dari inbox (langkah 12; langkah 8 TC-AC-ACC-153), pindah surface log.
- Temuan untuk QA:
  - TC-153 dan TC-154 bertanda Manual Only (inbox email asli); spec memakai mail-catcher dengan baseline (R-11).
  - TC-153 butir b ("Tautan aktivasi awal tidak dapat dipakai untuk aktivasi") tidak menyebut tampilan halaman tautan; spec memverifikasi dengan redaksi TC.
  - TC-154 langkah 7 ("Aktifkan term pertama FAMS dari License Allocation > Client Subscription") tidak menyebut langkah rincinya; spec menulis langkah apa adanya dan kemampuan itu di Prerequisites.
  - TC-154 Post Condition ("Fixture C-EDT-1 terpakai") menegaskan fixture tidak dapat dipakai ulang; spec men-seed fixture baru per run.

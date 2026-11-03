---
id: TC-AC-ACC-E2E-072-edit-activation-email-otomatis-saat-email-default-user-diubah-af
title: "Edit Email Default User Not Yet Activated: Activation Email Otomatis Hanya Bila Ada Term Aktif atau Expired (Active-Full)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-633
  - TC-AC-ACC-634
  - TC-AC-ACC-635
coverage:
  web: automated
---

# Edit Email Default User Not Yet Activated: Activation Email Otomatis Hanya Bila Ada Term Aktif atau Expired (Active-Full)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Dataset seed (nama bersuffix, Default User Not Yet Activated): `PT Berakhir Belum Aktivasi {runId}-072` (replika C-LIF-5: Active, FAMS Expired, Email Default User awal `berakhir.awal+{runId}-072@qwertysystem.net`), `PT Cahaya Baru {runId}-072` (replika C-07: FAMS Waiting for Approval), `PT Mulai Esok {runId}-072` (replika C-08: FAMS Pending). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Baseline (S-12): jumlah baris hasil Search nama unik pada Changelog sebelum aksi; format Modified By `[First Name] [Last Initial]` (R-14).
- Cleanup: hook `after` menghapus Client seed lewat API.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-633: Term FAMS Expired, Activation Email baru terkirim

1. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Berakhir Belum Aktivasi {runId}-072`, tekan Enter
2. Catat jumlah baris hasil Search sebagai N1
3. Tutup modal Changelog
4. Ketik Search `PT Berakhir Belum Aktivasi {runId}-072`, tekan Enter
5. Buka `⋯` baris `PT Berakhir Belum Aktivasi {runId}-072` lalu klik `Edit`
6. Catat nilai Email Default User yang terisi sebagai Email awal
7. Ubah Email Default User menjadi `ba.baru+{runId}-072@qwertysystem.net`
8. Klik `[Save]`
9. Verifikasi toast sukses edit "Success, client has been updated."
10. Verifikasi toast sukses "Success, activation email has been sent." tampil sesudah toast sukses edit
11. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Berakhir Belum Aktivasi {runId}-072`, tekan Enter
12. Verifikasi jumlah baris menjadi N1 + 2
13. Verifikasi dua baris teratas (Date terbaru, bertanggal hari ini, urutan bebas) ber-Client Name "PT Berakhir Belum Aktivasi {runId}-072" dan Modified By aktor: Action `Edit`, Field `Default User Email`, Old Value Email awal, New Value `ba.baru+{runId}-072@qwertysystem.net`; Action `Resend Activation Email`, Field `Email`, Old Value `—`, New Value `ba.baru+{runId}-072@qwertysystem.net`
14. Tutup modal Changelog

### TC-634: Term hanya Waiting for Approval, tanpa Activation Email

15. Ketik Search `PT Cahaya Baru {runId}-072`, tekan Enter
16. Buka `⋯` baris `PT Cahaya Baru {runId}-072` lalu klik `Edit`
17. Ubah Email Default User menjadi `cb.baru+{runId}-072@qwertysystem.net`
18. Klik `[Save]`
19. Verifikasi toast sukses "Success, client has been updated."
20. Verifikasi toast "Success, activation email has been sent." tidak tampil
21. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Cahaya Baru {runId}-072`, tekan Enter
22. Verifikasi modal Changelog memuat baris Action `Edit` untuk "PT Cahaya Baru {runId}-072" (anchor)
23. Verifikasi modal Changelog tidak memuat baris Action `Resend Activation Email` untuk "PT Cahaya Baru {runId}-072"
24. Tutup modal Changelog

### TC-635: Term hanya Pending, tanpa Activation Email

25. Ketik Search `PT Mulai Esok {runId}-072`, tekan Enter
26. Buka `⋯` baris `PT Mulai Esok {runId}-072` lalu klik `Edit`
27. Ubah Email Default User menjadi `me.baru+{runId}-072@qwertysystem.net`
28. Klik `[Save]`
29. Verifikasi toast sukses "Success, client has been updated."
30. Verifikasi toast "Success, activation email has been sent." tidak tampil
31. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Mulai Esok {runId}-072`, tekan Enter
32. Verifikasi modal Changelog memuat baris Action `Edit` untuk "PT Mulai Esok {runId}-072" (anchor)
33. Verifikasi modal Changelog tidak memuat baris Action `Resend Activation Email` untuk "PT Mulai Esok {runId}-072"

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Langkah penghubung (S-03): baseline Changelog, Search nama unik, penutupan modal Changelog.
- Asersi absence TC-634 dan TC-635 didahului toast sukses edit (anchor server selesai) dan baris `Edit` yang memuat Client sama pada surface yang sama (butir 8b-2).
- Temuan untuk QA:
  - TC-633 sampai TC-635 menamai Email awal yang dicatat pada langkah 3 tanpa nilai; spec membaca nilai dari popup Edit.
  - TC-634 dan TC-635 Expected butir c mensyaratkan "tidak memuat baris Resend Activation Email" tanpa anchor positif; spec menambah Verifikasi baris `Edit` sebagai anchor (butir 8b-2).

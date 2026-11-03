---
id: TC-AC-ACC-E2E-073-edit-resilience-5xx-dan-email-service-gagal-af
title: "Edit Client: Resilience 5xx dan Email Service Gagal Saat Edit Email Default User (Active-Full)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-164
  - TC-AC-ACC-155
coverage:
  web: automated
---

# Edit Client: Resilience 5xx dan Email Service Gagal Saat Edit Email Default User (Active-Full)

## Prerequisites

- Mode: FE+BE dengan intercept (TC-164) dan pemicu kegagalan sisi server (TC-155).
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya. `{r6}` = 6 digit terakhir `{runId}` (dipakai agar Client Code tetap maksimal 15 karakter).
- Dataset seed (nama bersuffix): Client `PT Sejahtera Abadi {runId}-073` (replika C-01: Active, Partner CV Mitra Sejati, Group Area Jakarta, Client Code `SJA-{r6}`, Default User Activated, PIC Email awal `pic.old@example.com`) (target TC-164); Client `PT Berakhir Belum Aktivasi {runId}-073` (replika C-LIF-5: Active, FAMS Expired, Default User Not Yet Activated, Email awal `berakhir.awal+{runId}-073@qwertysystem.net`; target TC-155). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Kebutuhan intercept (TC-164): respons request Edit Client dipaksa 500 lalu dilepas. Kemampuan teknis (TC-155): memaksa email service gagal (5xx) pada setiap percobaan kirim (disediakan tim FE/BE; endpoint tidak dikarang); membaca jumlah notifikasi berstatus Unread pada dropdown notifikasi navbar; membaca Changelog dengan Search nama unik (ukuran halaman modal 100). Hook `after` melepas intercept dan memulihkan email service.
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-164: Edit gagal 5xx

1. Ketik Search `PT Sejahtera Abadi {runId}-073`, tekan Enter
2. Buka `⋯` baris `PT Sejahtera Abadi {runId}-073` lalu klik `Edit`
3. Ubah Fax menjadi `0215550100`
4. Paksa respons request Edit 500 (intercept)
5. Klik `[Save]`
6. Verifikasi toast error "Error, failed to update client."
7. Verifikasi popup tetap terbuka
8. Verifikasi input dipertahankan (Fax "0215550100")
9. Lepas intercept
10. Klik `[✕]` di header popup
11. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
12. Klik `[Leave]`

### TC-155: Pengiriman otomatis Activation Email gagal

13. Buka dropdown notifikasi pada navbar, catat jumlah notifikasi Unread (N1), lalu tutup dropdown
14. Klik sub-tab Active
15. Ketik Search `PT Berakhir Belum Aktivasi {runId}-073`, tekan Enter
16. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Berakhir Belum Aktivasi {runId}-073`, tekan Enter
17. Ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Edit` (E0) dan jumlah baris Action `Resend Activation Email` (R0), lalu tutup modal
18. Paksa email service gagal (5xx)
19. Buka `⋯` baris `PT Berakhir Belum Aktivasi {runId}-073` lalu klik `Edit`
20. Ubah Email Default User menjadi `berakhir.baru+{runId}-073@qwertysystem.net`
21. Klik `[Save]`
22. Verifikasi toast sukses edit "Success, client has been updated."
23. Klik Company Name `PT Berakhir Belum Aktivasi {runId}-073` untuk membuka Detail
24. Verifikasi section Default User menampilkan email "berakhir.baru+{runId}-073@qwertysystem.net"
25. Verifikasi `[Resend Activation Email]` tersedia
26. Buka dropdown notifikasi pada navbar, catat jumlah Unread (N2), lalu tutup dropdown
27. Verifikasi N2 sama dengan N1 (belum ada notifikasi baru setelah percobaan pertama gagal)
28. Klik breadcrumb "Client" untuk kembali ke List
29. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Berakhir Belum Aktivasi {runId}-073`, tekan Enter
30. Ubah ukuran halaman modal menjadi 100, lalu hitung baris Action `Edit` (E1) dan baris Action `Resend Activation Email` (R1)
31. Verifikasi E1 sama dengan E0 + 1
32. Verifikasi baris Action `Edit` teratas (Date terbaru) ber-Field `Default User Email`, Old Value `berakhir.awal+{runId}-073@qwertysystem.net`, New Value `berakhir.baru+{runId}-073@qwertysystem.net`
33. Verifikasi R1 sama dengan R0 (pengiriman yang gagal tidak menulis baris `Resend Activation Email`)
34. Lepas simulasi kegagalan email service

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Pemulihan email service dan intercept dilakukan di hook `after` sebagai cadangan; langkah pelepasan eksplisit ditulis di akhir tiap blok.
- Langkah penghubung (S-03): Search nama unik, penutupan modal Changelog, breadcrumb "Client", penutup form dirty (S-08).
- Temuan untuk QA:
  - TC-155 mengasersi N2 = N1 setelah percobaan pertama gagal; notifikasi baru muncul hanya setelah percobaan ulang ketiga (spec TC-959). Spec ini tidak memajukan waktu.
  - TC-164 Expected tidak menyebut tombol `[Save]` aktif kembali; tidak diasersi.

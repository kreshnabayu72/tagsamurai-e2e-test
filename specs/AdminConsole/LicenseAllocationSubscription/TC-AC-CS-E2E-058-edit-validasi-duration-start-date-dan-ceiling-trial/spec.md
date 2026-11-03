---
id: TC-AC-CS-E2E-058-edit-validasi-duration-start-date-dan-ceiling-trial
title: "Edit: Validasi Duration, Start Date, dan Ceiling Trial"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-217
  - TC-AC-CS-218
  - TC-AC-CS-220
  - TC-AC-CS-221
  - TC-AC-CS-222
  - TC-AC-CS-620
coverage:
  web: automated
---

# Edit: Validasi Duration, Start Date, dan Ceiling Trial

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): capability Create saja Distributor PT Maju Bersama, Fajar Nugroho (Pre-setup #6), `createOnlySub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_CREATE_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data Pre-setup (milik aktor, dibaca; tidak ada perubahan disimpan): `SUBS-20260819-00001` Client Apotek Sehat Sentosa FAMS Growth Waiting for Approval, Duration 1 year(s) (#49); `SUBS-20260817-00003` Client Toko Sumber Rezeki SAMS Growth Waiting for Approval, Start Date tersimpan `15/08/26` (sudah lewat dari `19/08/26`) (#114); `SUBS-20260819-00004` Trial Client PT Bintang Timur FAMS Growth Waiting for Approval (#59); `SUBS-20260817-00004` Trial SIEM Client CV Nusantara Data Waiting for Approval, Log Source Quota 10 (#105); Ceiling Trial `Max Trial Duration` 60 day(s), `Max Trial Asset Quota` 200 assets, `Max Trial Concurrent User Quota` 50 users (#25); tanggal acuan uji `19/08/26`.
- Data Dinamis: tidak ada; setiap form Edit ditutup dengan `[Leave]` sehingga record tidak berubah.
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu untuk tanggal acuan `19/08/26` (jam server dan jam browser, dipulihkan di hook `after`).

## Test Steps

### TC-AC-CS-620: Field Duration pada Edit hanya menerima digit

1. Ketik Search `Apotek Sehat Sentosa`, tekan Enter, klik ikon `⋯` pada baris `SUBS-20260819-00001` lalu pilih `Edit`
2. Ketik `abc` dan `1.5` pada field Duration
3. Verifikasi huruf tidak masuk ke field Duration
4. Verifikasi nilai desimal tidak diterima sehingga Duration tetap bilangan bulat tahun

### TC-AC-CS-217: Validasi Duration kosong pada Edit

5. Kosongkan Duration lalu klik `[Save]`
6. Verifikasi error inline "Duration must not be empty"
7. Verifikasi modal tetap terbuka

### TC-AC-CS-218: Validasi Duration kurang dari 1 pada Edit

8. Isi Duration `0` lalu klik `[Save]`
9. Verifikasi error inline "Duration must be at least 1 year"
10. Klik `[✕]`, verifikasi dialog Unsaved Changes, lalu klik `[Leave]`
11. Klik ikon `⋯` pada baris `SUBS-20260819-00001` lalu pilih `Edit`
12. Verifikasi Duration tersimpan tetap `1` (data tidak berubah)
13. Klik `[✕]`

### TC-AC-CS-220: Start Date tersimpan term Waiting for Approval sudah lewat ditolak sampai diperbarui

14. Ganti isi kotak search dengan `Toko Sumber Rezeki`, tekan Enter, klik ikon `⋯` pada baris `SUBS-20260817-00003` lalu pilih `Edit`
15. Ubah Duration saja lalu klik `[Save]`
16. Verifikasi Save ditolak dengan error inline "Start date cannot be in the past"
17. Verifikasi modal tetap terbuka dan Start Date tersimpan `15/08/26` tidak berubah
18. Klik `[✕]`, verifikasi dialog Unsaved Changes, lalu klik `[Leave]`

### TC-AC-CS-221: Edit Trial di atas ceiling ditolak

19. Ganti isi kotak search dengan `PT Bintang Timur`, tekan Enter, klik ikon `⋯` pada baris `SUBS-20260819-00004` lalu pilih `Edit`
20. Isi Trial Duration `61`, Trial Asset Quota `201`, Trial Concurrent User Quota `51`
21. Verifikasi error "Trial duration cannot exceed 60 days"
22. Verifikasi error "Trial asset quota cannot exceed 200"
23. Verifikasi error "Trial concurrent user quota cannot exceed 50"
24. Verifikasi `[Save]` Disabled selama error real-time

### TC-AC-CS-222: Edit Trial dengan nilai kosong dan Log Source di luar batas

25. Kosongkan Trial Duration lalu isi Trial Asset Quota `0`
26. Verifikasi error "Trial duration must not be empty"
27. Verifikasi error "Trial asset quota must be at least 1"
28. Verifikasi `[Save]` Disabled selama error
29. Klik `[✕]`, verifikasi dialog Unsaved Changes, lalu klik `[Leave]`
30. Ganti isi kotak search dengan `CV Nusantara Data`, tekan Enter, klik ikon `⋯` pada baris `SUBS-20260817-00004` lalu pilih `Edit`
31. Isi Trial Log Source Quota `10000`
32. Verifikasi error "Trial log source quota must be between 1 and 9999"
33. Verifikasi `[Save]` Disabled selama error
34. Klik `[✕]`, verifikasi dialog Unsaved Changes, lalu klik `[Leave]`

## Notes

- Urutan menyimpang dari urutan TC sumber (S-10): TC-AC-CS-620 paling awal dan TC-AC-CS-217 dan TC-AC-CS-218 berurutan pada satu pembukaan Edit record `SUBS-20260819-00001`; TC-AC-CS-221 dan bagian pertama TC-AC-CS-222 berurutan pada satu pembukaan Edit trial FAMS.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16); `✕`, dialog `Unsaved Changes`, dan `[Leave]` menutup form dirty (S-08, S-09).
- Temuan untuk QA: (1) TC-AC-CS-220 Expected c ("Rebase tanggal hanya terjadi saat Approve") tidak punya langkah observasi sehingga tidak diasersi. (2) TC-AC-CS-217 dan TC-AC-CS-218 "Data tidak berubah" diasersi dengan membuka ulang Edit setelah `[Leave]` karena TC tidak menyebut layar pengamatan.
- Alasan melewati sekitar 35 langkah bila dihitung penuh: semua blok satu topik (validasi form Edit) tanpa kelas harness lain, berdiri sendiri, dan memakai record milik aktor yang sama.

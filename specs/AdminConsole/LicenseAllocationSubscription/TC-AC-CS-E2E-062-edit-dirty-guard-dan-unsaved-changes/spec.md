---
id: TC-AC-CS-E2E-062-edit-dirty-guard-dan-unsaved-changes
title: "Edit: Dirty Guard dan Unsaved Changes"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-237
  - TC-AC-CS-543
  - TC-AC-CS-544
  - TC-AC-CS-559
coverage:
  web: automated
---

# Edit: Dirty Guard dan Unsaved Changes

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): capability Create saja Distributor PT Maju Bersama, Fajar Nugroho (Pre-setup #6), `createOnlySub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_CREATE_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data Pre-setup (milik aktor): `SUBS-20260819-00001` Client Apotek Sehat Sentosa FAMS Growth Waiting for Approval, Duration 1 (#49).
- Data Dinamis: tidak ada; semua perubahan form dibuang lewat `[Leave]` sehingga record tidak berubah dan tidak ada entri log baru.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Changelog Client `Apotek Sehat Sentosa` — FAMS.

## Test Steps

### TC-AC-CS-237: Menutup Edit yang dirty memunculkan Unsaved Changes dan nilai dikembalikan dianggap clean

1. Ketik Search `Apotek Sehat Sentosa`, tekan Enter, lalu catat jumlah entri Changelog Client `Apotek Sehat Sentosa` — FAMS sebagai baseline
2. Klik ikon `⋯` pada baris `SUBS-20260819-00001` lalu pilih `Edit`
3. Klik `[✕]` tanpa mengubah apa pun
4. Verifikasi tanpa perubahan modal tertutup langsung tanpa dialog
5. Klik ikon `⋯` pada baris `SUBS-20260819-00001` lalu pilih `Edit`
6. Ubah Duration menjadi `2` dan klik `[✕]`
7. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" muncul dengan tombol `[Cancel]` dan `[Leave]`
8. Klik `[Cancel]`
9. Ubah Duration kembali ke `1` dan klik `[✕]`
10. Verifikasi setelah nilai identik dengan nilai tersimpan modal tertutup tanpa dialog

### TC-AC-CS-544: Pilihan Cancel pada dialog Unsaved Changes Edit mempertahankan perubahan

11. Klik ikon `⋯` pada baris `SUBS-20260819-00001` lalu pilih `Edit`
12. Ubah Duration menjadi `2` dan klik `[✕]`
13. Klik `[Cancel]`
14. Verifikasi dialog tertutup dan modal Edit tetap terbuka
15. Verifikasi Duration `2` dipertahankan pada field

### TC-AC-CS-559: Klik backdrop tidak menutup form Edit walau dirty

16. Klik area gelap di luar modal
17. Verifikasi modal Edit tetap terbuka dengan Duration `2` dipertahankan
18. Verifikasi dialog Unsaved Changes tidak muncul

### TC-AC-CS-543: Pilihan Leave pada dialog Unsaved Changes Edit membuang perubahan

19. Klik `[✕]`
20. Verifikasi dialog Unsaved Changes muncul
21. Klik `[Leave]`
22. Verifikasi dialog dan modal Edit tertutup tanpa menyimpan, tanpa toast
23. Klik ikon `⋯` pada baris `SUBS-20260819-00001` lalu pilih `Edit`
24. Verifikasi Duration tersimpan tetap `1` (Edit yang dibuka kembali; record tidak berubah)
25. Verifikasi jumlah entri Changelog Client `Apotek Sehat Sentosa` — FAMS sama dengan baseline
26. Klik `[✕]`

## Notes

- Urutan menyimpang dari urutan TC sumber (S-10): TC-AC-CS-544, TC-AC-CS-559, dan TC-AC-CS-543 dirangkai pada satu form dirty yang sama (nilai Duration `2`); TC-AC-CS-543 yang membuang perubahan paling akhir.
- Observasi "belum tersimpan ke record" (TC-AC-CS-544 butir b, TC-AC-CS-559 butir c) dan "Duration pada baris tetap 1" (TC-AC-CS-543 butir b) diamati sekali dengan membuka ulang Edit setelah `[Leave]`, karena kasus-kasus itu berbagi record dan satu pembuangan perubahan.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16); `✕` menutup modal Edit bersih tanpa dialog.
- Temuan untuk QA: TC-AC-CS-543 butir b menyebut "Duration pada baris" padahal List tidak punya kolom Duration; spec mengamatinya di form Edit yang dibuka kembali.

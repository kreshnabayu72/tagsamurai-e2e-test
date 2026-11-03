---
id: TC-AC-CS-E2E-061-edit-group-manager-bypass
title: "Edit: Group Manager Bypass"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-219
  - TC-AC-CS-225
  - TC-AC-CS-226
  - TC-AC-CS-227
  - TC-AC-CS-228
coverage:
  web: automated
---

# Edit: Group Manager Bypass

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Group Manager scope Group Jawa Distributor PT Maju Bersama, Dewi Anggraini (Pre-setup #5), `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_GM_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data Pre-setup baca-saja/global: Group Manager `Dewi Anggraini` (#5) bypass; Main Pocket PT Maju Bersama (#20); harga feature plan FAMS Professional $10,000.00 per tahun (#27); tanggal acuan uji `19/08/26` (#28).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`; Client binaan PT Maju Bersama pada group `Jawa`, term milik requester Group Manager `Dewi A`, Plan Owner PT Maju Bersama; Subscription ID tiap term dibaca lewat API seeding dan dirujuk di langkah sebagai Subscription ID seed pada Client yang bersangkutan). Satu seed per blok TC:
  1. TC-AC-CS-219: Client `Percetakan Mega A+{runId}-061` dengan term FAMS Professional Pending, Start Date `15/09/26`, End Date `14/09/27`, Duration 1 year(s), Reserve $10,000.00 (bentuk Pre-setup #57).
  2. TC-AC-CS-228: Client `Toko Sumber Rezeki B+{runId}-061` dengan term FAMS Professional Pending beralokasi dua lisensi Pending (Concurrent User 10 dan Maintenance 5) pada ledger term, tanggal `15/09/26` / `14/09/27` (bentuk Pre-setup #75 dan #97).
  3. TC-AC-CS-225: Client `Percetakan Mega B+{runId}-061`, term berbentuk sama dengan seed TC-AC-CS-219.
  4. TC-AC-CS-226: Client `Percetakan Mega C+{runId}-061`, term berbentuk sama dengan seed TC-AC-CS-219.
  5. TC-AC-CS-227: Client `Toko Sumber Rezeki A+{runId}-061`, term berbentuk sama dengan seed TC-AC-CS-228.
- Data Dinamis: hasil Edit, status term, Reserve, dan entri audit trail hanya pada Client seed dan dihapus bersama seed di hook `after`. Yang dipulihkan hanya state global: saldo kantong alokasi kedua (diubah TC-AC-CS-228 untuk memicu penolakan saldo; dipulihkan oleh fixture backend pemulihan state di langkah penghubung dan di hook `after`; Wallet bersama tidak dapat dimiliki spec) dan jam server dan browser (hook `after`).
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu untuk tanggal acuan `19/08/26` (jam server dan jam browser, dipulihkan di hook `after`); membaca saldo Reserved, Captured, dan Available Wallet Main Pocket; mengatur saldo kantong alokasi kedua kurang dari kebutuhan End Date baru; membaca jumlah entri Changelog.

## Test Steps

### TC-AC-CS-219: Validasi Start Date sebelum hari ini pada Edit mode New

1. Ketik Search `Percetakan Mega A+{runId}-061`, tekan Enter, klik ikon `⋯` pada baris Subscription ID seed Percetakan Mega A lalu pilih `Edit`
2. Isi Start Date `18/08/26` lalu klik `[Save]`
3. Verifikasi error inline "Start date cannot be in the past"
4. Klik `[✕]`, verifikasi dialog Unsaved Changes, lalu klik `[Leave]`
5. Klik ikon `⋯` pada baris Subscription ID seed Percetakan Mega A lalu pilih `Edit`
6. Verifikasi Start Date tersimpan tetap `15/09/26` (data tidak berubah)

### TC-AC-CS-228: Saldo salah satu alokasi kurang menolak seluruh Edit

7. Klik `[✕]`, atur saldo kantong alokasi kedua kurang dari kebutuhan End Date baru lewat fixture backend, lalu ganti isi kotak search dengan `Toko Sumber Rezeki B+{runId}-061`, tekan Enter
8. Klik ikon `⋯` pada baris term Pending beralokasi lalu pilih `Edit`
9. Ubah Duration menjadi `3` lalu klik `[Save]`
10. Verifikasi dialog blok dengan Title "Cannot Update Subscription"
11. Verifikasi Body "• Toko Sumber Rezeki B+{runId}-061 — FAMS" dan "Insufficient wallet balance"
12. Verifikasi tombol tunggal `[OK]`
13. Klik `[OK]`, klik `[✕]`, verifikasi dialog Unsaved Changes, lalu klik `[Leave]`
14. Buka Detail term; License Quota tampil
15. Verifikasi term dan kedua alokasi tidak berubah
16. Pulihkan saldo kantong alokasi kedua ke keadaan awal lewat fixture backend

### TC-AC-CS-225: Edit term Pending oleh bypass GM tetap Pending dan Reserve disesuaikan

17. Kembali ke List, ganti isi kotak search dengan `Percetakan Mega B+{runId}-061`, tekan Enter, lalu klik ikon `⋯` pada baris Subscription ID seed Percetakan Mega B dan pilih `Edit`
18. Ubah Duration menjadi `2` lalu klik `[Save]`
19. Verifikasi toast sukses "Success, subscription has been updated."
20. Verifikasi status baris Subscription ID seed Percetakan Mega B tetap Pending tanpa siklus approval baru
21. Verifikasi Reserve disesuaikan menjadi $20,000.00
22. Buka Detail baris Subscription ID seed Percetakan Mega B
23. Verifikasi End Date menjadi `14/09/28`

### TC-AC-CS-226: Edit Start Date term Pending menjadi hari ini langsung Active dengan dua record log

24. Kembali ke List, ganti isi kotak search dengan `Percetakan Mega C+{runId}-061`, tekan Enter, lalu catat jumlah entri Changelog Client `Percetakan Mega C+{runId}-061` — FAMS sebagai baseline
25. Klik ikon `⋯` pada baris Subscription ID seed Percetakan Mega C lalu pilih `Edit`
26. Ubah Start Date menjadi `19/08/26` lalu klik `[Save]`
27. Verifikasi toast sukses "Success, subscription has been updated."
28. Verifikasi status baris menjadi Active dengan Start Date `19/08/26`
29. Verifikasi Reserve di-Capture
30. Buka modal Changelog Client `Percetakan Mega C+{runId}-061` — FAMS
31. Verifikasi jumlah entri Changelog bertambah tepat dua dibanding baseline
32. Verifikasi entri Action `Edit (Start Date, mode New)`, Field `Start Date`, Old `15/09/26`, New `19/08/26`, Modified By `Dewi A`
33. Verifikasi entri Action `Activate (Save Edit, mode New dengan Start Date hasil edit = hari ini; aktor)`, Field `Status`, Old `Pending`, New `Active`, Modified By `Dewi A`

### TC-AC-CS-227: Edit term Pending beralokasi menghitung ulang tanggal kedaluwarsa dan biaya alokasi

34. Tutup modal Changelog, ganti isi kotak search dengan `Toko Sumber Rezeki A+{runId}-061`, tekan Enter, klik ikon `⋯` pada baris term Pending beralokasi lalu pilih `Edit`
35. Ubah Duration menjadi `2` lalu klik `[Save]`
36. Verifikasi toast sukses "Success, subscription has been updated."
37. Buka Detail term; License Quota tampil
38. Verifikasi tanggal kedaluwarsa dan biaya kedua alokasi dihitung ulang mengikuti End Date baru dan Reserve tiap alokasi disesuaikan
39. Verifikasi kedua alokasi tetap Pending tanpa approval ulang

## Notes

- Urutan menyimpang dari urutan TC sumber (S-10): TC-AC-CS-219 (validasi diblokir) dan TC-AC-CS-228 (penolakan saldo) didahulukan sebelum Edit sukses TC-AC-CS-225, TC-AC-CS-226, dan TC-AC-CS-227. Tiap blok memakai Client seed sendiri sehingga urutan tidak mengubah state blok lain.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16); `✕`, dialog `Unsaved Changes`, dan `[Leave]` menutup form dirty (S-08, S-09); kembali ke List dari Detail; tutup modal Changelog sebelum aksi berikutnya; pemulihan saldo kantong alokasi lewat fixture; log dicari berdasarkan Action dan Field, bukan posisi teratas (S-14).
- Temuan untuk QA: (1) TC-AC-CS-227 Expected b tidak menyebut tanggal kedaluwarsa dan biaya angka; spec mengasersi dihitung ulang tanpa nilai. (2) TC-AC-CS-228 tidak menyebut ID baris term `Toko Sumber Rezeki` Pre-setup #75; spec mencarinya lewat Search nama Client. (3) TC-AC-CS-226 menyebut Reserve di-Capture tanpa layar pengamatan; spec memakai kemampuan baca Wallet disediakan tim FE/BE.
- Spec ini 39 langkah, di atas smell 35 langkah. Alasan: semua blok satu topik (Edit oleh Group Manager bypass) pada record dalam scope aktor yang sama, tanpa kelas harness lain; kegagalan satu blok tidak membuat blok lain kehilangan makna.

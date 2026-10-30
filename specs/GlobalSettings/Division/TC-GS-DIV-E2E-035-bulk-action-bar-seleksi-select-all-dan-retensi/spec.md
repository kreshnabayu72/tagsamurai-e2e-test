---
id: TC-GS-DIV-E2E-035-bulk-action-bar-seleksi-select-all-dan-retensi
title: "Bulk Action Bar: Screening, Counter, Checkbox Header, Select All Lintas Halaman, dan Retensi Seleksi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-125
  - TC-GS-DIV-126
  - TC-GS-DIV-127
  - TC-GS-DIV-128
  - TC-GS-DIV-160
coverage:
  web: automated
---

# Bulk Action Bar: Screening, Counter, Checkbox Header, Select All Lintas Halaman, dan Retensi Seleksi

## Prerequisites

- Mode: FE+BE. Spec hanya memilih baris dan tidak menekan aksi yang menghapus; tidak ada data diubah atau dihapus.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor dan navigasi ke Global Settings > User > Division dilakukan di hook `before` spec ini (seedSession, kredensial dari env var). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tetap di environment, tidak diubah): 6 Division (Finance, Human Resources, Legal, Operations, Compliance, Treasury).
- Data dinamis: Population D-02 (26 Division literal `Accounting` sampai `Warehouse`, setara TC-GS-DIV-30; nama literal tanpa suffix karena asersi bergantung pada nama `Accounting` dan `Administration` serta jumlah 32 baris; pengecualian S-12). Seeding lewat API di hook `before`, idempotent: nama yang sudah ada dilewati, dan cleanup di hook `after` hanya menghapus Division yang dibuat hook `before` spec ini. Fixture belum ada; tim FE menyiapkan kunci `populationD02` (26 nama dan Code). Total tabel harus 32 baris tanpa filter (6 Pre-setup + 26 Population, halaman 1 berisi 10 baris dan total 4 halaman) saat spec berjalan; suite berjalan serial dan spec lain membersihkan datanya sendiri.
- Selection Limit entitas tidak diubah dan lebih besar dari 32 (default entitas). Page size tabel default 10.
- Cleanup di hook `after`: hapus Division Population yang dibuat hook `before`, hapus isi kotak Search (`(←)`), dan bersihkan seleksi tabel. Hook `beforeEach`: tutup dialog atau dropdown yang terbuka lalu kembali ke Global Settings > User > Division.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-DIV-125: Screening Bulk Action Bar saat satu baris dicentang

1. Centang checkbox baris `Accounting`
2. Verifikasi Bulk Action Bar muncul
3. Verifikasi urutan elemen Bulk Action Bar: tombol `Bulk Action`, teks `1 Division selected`, tombol `Select All (32 records)`, icon `(✕)`
4. Klik tombol `Bulk Action`
5. Verifikasi dropdown `Bulk Action` memuat aksi `Delete`
6. Verifikasi aksi `Delete` berseverity danger
7. Tutup dropdown `Bulk Action` tanpa memilih aksi

### TC-GS-DIV-126: Counter Bulk Action Bar bertambah dan berkurang realtime serta clear lewat X

8. Centang checkbox baris `Administration`
9. Verifikasi counter `2 Divisions selected`
10. Hilangkan centang baris `Accounting`
11. Verifikasi counter `1 Division selected`
12. Klik icon `(✕)` pada Bulk Action Bar
13. Verifikasi seluruh seleksi dibatalkan
14. Verifikasi Bulk Action Bar tertutup

### TC-GS-DIV-127: Checkbox header memilih seluruh baris halaman dan status indeterminate

15. Klik checkbox header
16. Verifikasi 10 baris halaman 1 checked
17. Verifikasi counter `10 Divisions selected`
18. Klik checkbox header lagi
19. Verifikasi seluruh baris unchecked
20. Verifikasi Bulk Action Bar hilang
21. Centang checkbox baris `Accounting`
22. Verifikasi checkbox header berstatus indeterminate `[-]`
23. Verifikasi counter `1 Division selected`

### TC-GS-DIV-128: Select All lintas halaman memilih seluruh baris dan toggle menjadi Unselect All

24. Klik `Select All (32 records)`
25. Verifikasi seluruh 32 baris terselect: counter `32 Divisions selected`
26. Verifikasi tombol berubah menjadi `Unselect All`
27. Pindah ke halaman 2
28. Verifikasi baris pada halaman 2 tetap checked
29. Klik `Unselect All`
30. Verifikasi seluruh seleksi dibatalkan
31. Verifikasi Bulk Action Bar tertutup

### TC-GS-DIV-160: Seleksi checkbox bertahan saat Search dikosongkan

32. Ketik Search `Accounting`, tekan Enter
33. Centang checkbox baris `Accounting`
34. Kosongkan isi kotak search dengan `(✕)`, tekan Enter
35. Verifikasi baris `Accounting` tetap tercentang
36. Verifikasi counter `1 Division selected` tetap tampil
37. Klik icon `(✕)` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC. Langkah 1 adalah langkah 1 TC-125 sekaligus kondisi awal TC-126: langkah "Centang baris `Accounting`" TC-126 sumber dipenuhi oleh seleksi `Accounting` dari TC-125, sehingga TC-126 melanjutkan dengan mencentang `Administration`. Langkah 21 (TC-127) adalah langkah "Centang 1 baris saja" TC-127 dan menjadi seleksi awal TC-128 (langkah "Centang 1 baris" TC-128 sumber digabung ke langkah 21).
- Butir Expected TC-128 diurutkan menurut state: tombol berubah `Unselect All` (butir c) diasersi sebelum pindah ke halaman 2 (langkah 26), baru baris halaman 2 tetap checked (butir b, langkah 28), karena toggle tombol adalah state yang berubah setelah halaman berganti (bagian 8b butir 5 dan S-14). Butir a ("Seluruh 32 baris terselect dan counter menampilkan `32 Divisions selected`") diasersi di langkah 25 sebagai satu `Verifikasi`: seluruh baris terselect teramati lewat counter `32 Divisions selected`. Baris halaman 2 tetap checked (langkah 28) adalah butir b.
- Langkah penghubung (aksi tanpa `Verifikasi`): 4 dan 7 (membuka dan menutup dropdown `Bulk Action` untuk mengamati aksi `Delete`; TC sumber menyebut aksi `Delete` pada tombol `Bulk Action` tanpa langkah membukanya), 37 (membersihkan seleksi akhir).
- Tidak ada aksi yang menghapus data di spec ini; Bulk Delete diuji di spec 037, 038, 039, dan 040.
- Spec melewati sekitar 35 langkah (37 langkah) karena memuat lima TC Bulk Action Bar pada satu kelas harness (fungsional), satu layar, dan satu dataset 32 baris. Blok saling melanjutkan state: TC-126 memakai seleksi `Accounting` dari TC-125 dan TC-128 memakai seleksi langkah 21 TC-127; memisahkannya mengulang login, seeding Population, dan pembentukan seleksi yang sama. Tidak ada aksi yang menghapus data.
- Temuan untuk QA:
  - TC-126, TC-127, dan TC-128 tidak menyatakan state awal seleksi; spec melanjutkan seleksi TC sebelumnya bila TC berikutnya membutuhkannya (TC-126 dari TC-125, TC-128 dari TC-127) dan membersihkan seleksi sebelum TC-160 lewat langkah 29 (hasil diverifikasi langkah 30 dan 31).
  - TC-127 butir a menyebut "halaman 1 (10 baris)" dan TC-125 menyebut `Select All (32 records)`; keduanya mensyaratkan Population D-02 (32 baris) tanpa Division lain milik spec lain.
  - TC-160 tidak menyebut cara membuka Search (reveal toolbar); spec membuka Search lewat langkah atomik `Ketik Search` (bagian 8b butir 9).
  - TC-125 Post Condition tidak ada; TC-126, TC-127, TC-128, dan TC-160 tanpa Post Condition.

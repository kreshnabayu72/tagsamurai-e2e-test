---
id: TC-FA-LIC-E2E-141-changelog-allocation-quota-paginasi-25-entri
title: "Paginasi Modal Changelog Allocation Quota dengan 25 Entri: Page Size, Nomor Halaman, Sort, Search, dan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-357
  - TC-FA-LIC-358
  - TC-FA-LIC-359
coverage:
  web: automated
---

# Paginasi Modal Changelog Allocation Quota dengan 25 Entri: Page Size, Nomor Halaman, Sort, Search, dan Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data: riwayat Changelog Allocation Quota Pre-setup #42 (25 entri): 6 entri Pre-setup #27 ditambah 19 entri fixture bertanggal sebelum 25/09/26 08:45 (Action `Edit`, Field `Allocated Quota`; Group Name dan Modified By memakai nama yang sudah ada di Pre-setup #27), sehingga Search `Allocated Quota` dan Filter Action `Edit` mengembalikan lebih dari 10 baris. Fixture entri tambahan disediakan tim FE/BE; hook `before` menjalankan fixture BE pemulih riwayat Pre-setup #27 lebih dulu, lalu menambah entri, dan hook `after` memulihkan riwayat ke Pre-setup #27 lewat fixture BE pemulih riwayat.
- Kemampuan teknis: klik di luar daftar pilihan page size untuk menutupnya tanpa memilih; tombol `Esc` tidak dipakai.
- Pengecualian S-12 `[KEPUTUSAN 2026-11-02]`: fixture BE pemulih riwayat Pre-setup #27 dijalankan di hook `before` sebelum 19 entri (Pre-setup #42) ditambahkan; suite serial (`parallel: false`); asersi absolut jumlah dan urutan baris Changelog Allocation Quota (langkah 3, 10, dan 13) hanya valid tepat setelah pemulihan itu (A-17).
- Spec ini tidak mengubah state global; Sort dan Search yang diubah spec dikembalikan ke netral dan kosong di akhir blok.

## Test Steps

### TC-FA-LIC-357: Default 10 per halaman, pilihan 10/25/50/100, input nomor halaman

1. Buka tab Allocation Quota pada node All Groups, klik ikon Changelog pada toolbar Level 1 Groups Quota
2. Verifikasi default 10 baris per halaman
3. Verifikasi halaman 1 menampilkan 10 baris
4. Buka pilihan page size
5. Verifikasi pilihan page size 10, 25, 50, 100 (tanpa opsi All)
6. Tutup pilihan page size tanpa memilih dengan klik di luar daftar
7. Verifikasi page size tetap 10
8. Ketik nomor halaman 2 pada input, tekan Enter
9. Verifikasi input nomor halaman 2 langsung membuka halaman 2
10. Verifikasi halaman 2 menampilkan 10 baris (baris ke-11 sampai ke-20)
11. Buka pilihan page size
12. Pilih 25
13. Verifikasi seluruh 25 baris tampil dalam satu halaman
14. Verifikasi tabel kembali ke halaman 1

### TC-FA-LIC-358: Nomor halaman tidak valid diabaikan, ganti sort tetap di halaman, ganti page size ke halaman 1

15. Pilih page size 10
16. Pindah ke halaman 2
17. Ketik `0` pada input nomor halaman, tekan Enter
18. Ketik `99` pada input nomor halaman, tekan Enter
19. Ketik `abc` pada input nomor halaman, tekan Enter
20. Verifikasi input tidak valid diabaikan dan tabel tetap di halaman 2
21. Klik header kolom `Date` untuk sort
22. Verifikasi mengganti sort tetap di halaman 2
23. Klik header kolom `Date` dua kali lagi sampai netral
24. Ganti page size menjadi 25
25. Verifikasi mengganti page size kembali ke halaman 1

### TC-FA-LIC-359: Search dan Apply Filter di halaman lebih dari 1 mereset ke halaman 1

26. Pilih page size 10
27. Pindah ke halaman 2
28. Ketik Search `Allocated Quota`, tekan Enter
29. Verifikasi setelah Search tabel kembali ke halaman 1
30. Pindah ke halaman 2 lagi
31. Klik ikon Filter, pada `Action` pilih `Edit`, klik `[Apply]`
32. Verifikasi setelah Apply Filter tabel kembali ke halaman 1
33. Klik `[Clear Field]`, klik `[Apply]`, klik icon panah `(←)` di kiri toolbar, lalu tutup modal dengan `[×]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 15 dan 26 mengembalikan page size ke 10; langkah 23 mengembalikan sort ke netral; langkah 33 membersihkan filter dan Search lalu menutup modal (S-09).
- Temuan untuk QA:
  - TC-FA-LIC-358 langkah 4 tidak menyebut kolom sort; spec memakai `Date`.

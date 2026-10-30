---
id: TC-GS-POS-E2E-003-pagination-dan-ukuran-halaman-tabel-utama
title: "Pagination 10 Baris, Navigasi Halaman, Ukuran Halaman 10/25/50/100, dan Input Nomor Halaman Tabel Position"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-10
  - TC-GS-POS-11
  - TC-GS-POS-12
coverage:
  web: automated
---

# Pagination 10 Baris, Navigasi Halaman, Ukuran Halaman 10/25/50/100, dan Input Nomor Halaman Tabel Position

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > User > Position; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, tanpa suffix): Position 10 `IT Manager`, 11 `Finance Analyst`, 12 `Warehouse Supervisor`, 13 `Customer Success Manager`, 14 `Procurement Officer`, 15 `Field Technician`, 16 `Sales Coordinator` (7 record).
- Data Dinamis (di-seed lewat API di hook `before`; nama bersuffix per run; fixture baru `Fixture.position.pagingSeed003`): 8 Position `iOS Developer {runId}-003`, `Legal Counsel {runId}-003`, `Marketing Executive {runId}-003`, `Quality Assurance Analyst {runId}-003`, `Data Engineer {runId}-003`, `Office Administrator {runId}-003`, `Logistics Coordinator {runId}-003`, dan `Payroll Specialist {runId}-003`. Dengan 7 record Pre-setup, jumlah seluruh record Position N = 15 (memenuhi 11 ≤ N ≤ 20 pada precondition TC). N diturunkan dari seeding (7 Pre-setup + 8 Data Dinamis) dan dihitung oleh hook `before`, bukan dibaca dari tabel yang hanya menampilkan satu halaman (bagian 8b butir 10).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-003` yang masih ada.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true, lihat `suite.md`.
- Kemampuan teknis: pembacaan jumlah baris tabel dan teks tiap baris; interaksi Overlay Page Size dan input nomor halaman.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### TC-GS-POS-10: Pagination default 10 baris dan navigasi halaman

1. Amati jumlah baris halaman 1
2. Verifikasi halaman 1 menampilkan 10 baris
3. Catat nama 10 baris halaman 1
4. Klik tombol next
5. Verifikasi halaman 2 menampilkan N−10 baris sisanya
6. Verifikasi urutan baris halaman 2 lanjut Name A-Z setelah baris terakhir halaman 1
7. Klik tombol prev
8. Verifikasi prev kembali ke halaman 1
9. Verifikasi halaman 1 menampilkan 10 baris yang sama dengan yang dicatat sebelumnya

### TC-GS-POS-11: Pilihan ukuran halaman 10/25/50/100 tabel Position

10. Buka Overlay Page Size
11. Verifikasi Overlay Page Size berisi tepat `10 | 25 | 50 | 100`
12. Verifikasi Overlay Page Size tidak memiliki opsi `All`
13. Pilih 25
14. Verifikasi N baris tampil dalam 1 halaman
15. Buka Overlay Page Size
16. Pilih 50
17. Verifikasi N baris tampil dalam 1 halaman
18. Buka Overlay Page Size
19. Pilih 100
20. Verifikasi N baris tampil dalam 1 halaman
21. Buka Overlay Page Size
22. Pilih 10

### TC-GS-POS-12: Input nomor halaman langsung + Enter

23. Verifikasi ukuran halaman 10 sebagai kondisi awal
24. Verifikasi halaman aktif 1 sebagai kondisi awal
25. Ketik `2` pada input nomor halaman, tekan Enter
26. Verifikasi tabel langsung berpindah ke halaman 2
27. Verifikasi halaman 2 menampilkan N−10 baris

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan (10, 11, 12). Pembukaan Global Settings > User > Position dilakukan hook `beforeEach` dan dipakai bersama ketiga TC; tidak ada pembukaan ulang.
- Spec 003 (pagination) dan spec 004 (retensi state tabel) berbagi dataset Position yang sama dan sengaja dipisah: gabungannya 78 langkah (27 dan 51), jauh di atas sekitar 35 langkah, dan F5 pada TC-GS-POS-13 (spec 004) memuat ulang halaman sehingga kegagalan keras di blok itu menghilangkan makna blok pagination yang berjalan sesudahnya.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3 (mencatat nama 10 baris halaman 1 sebagai pembanding langkah 9) dan langkah 22 (mengembalikan ukuran halaman ke 10 sebagai kondisi awal TC-GS-POS-12). Pada TC-GS-POS-12 langkah 23 dan 24 memverifikasi precondition ukuran halaman 10 (dipulihkan pada langkah 22) dan halaman aktif 1.
- Langkah yang menampilkan N baris pada TC-GS-POS-11 mengasersi seluruh N baris dalam satu halaman (tidak ada halaman berikutnya); karena N ≤ 20, opsi 25, 50, dan 100 semuanya memuat seluruh baris.
- Temuan untuk QA:
  - Seeding mengikuti precondition TC-GS-POS-10, 11, dan 12 (11 ≤ N ≤ 20) dan Expected TC-GS-POS-11 (N baris dalam 1 halaman untuk opsi 100), dengan N = 15; batas atas ukuran halaman 100 dengan lebih dari 100 baris tidak teruji pada TC sumber ini.
  - TC sumber tidak menyatakan bahwa entitas Total Control tidak memuat Position selain Pre-setup 10 sampai 16; spec mengasumsikan N = 15 hanya dari 7 Pre-setup dan 8 Data Dinamis.
  - TC-GS-POS-12 tidak menyebut kondisi awal selain ukuran halaman 10; spec memverifikasi halaman 1 dan ukuran 10 sebagai kondisi awal.

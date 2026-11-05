---
id: TC-FA-TAG-E2E-229-pagination-tabel-grup-page-size-navigasi-dan-input-halaman
title: "Pagination Tabel Grup: Page Size, Navigasi Halaman, dan Input Nomor Halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-914
  - TC-FA-TAG-915
  - TC-FA-TAG-916
  - TC-FA-TAG-917
  - TC-FA-TAG-918
  - TC-FA-TAG-919
  - TC-FA-TAG-920
  - TC-FA-TAG-921
coverage:
  web: automated
---

# Pagination Tabel Grup: Page Size, Navigasi Halaman, dan Input Nomor Halaman

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk dataset tab Paired di bawah, termasuk penggantian dataset umum empat grup dengan dataset khusus 25 grup di hook `before` dan pemulihan ke dataset umum empat grup di hook `after`; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup tab Paired, dataset khusus pagination tabel grup (precondition d TC-FA-TAG-914 s.d. TC-FA-TAG-921; kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Grup acuan | Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0 | `grupAcuan` |
| Jumlah baris grup | Scope akun Total Control memuat total 25 baris grup (empat grup acuan ditambah 21 grup lain); page size bawaan 10 sehingga ada 3 halaman (halaman 3 memuat baris ke-21 sampai ke-25) | `grup25Baris` |

- State yang diubah: state tampilan tabel (page size dan halaman) dan dataset tab Paired (diganti ke dataset khusus 25 grup di hook `before`, dipulihkan ke dataset umum empat grup di hook `after` yang tetap jalan walau spec gagal); tidak ada perubahan data bisnis lain. Page size dikembalikan ke 10 oleh langkah 13 dan hook `beforeEach` suite membuka halaman TAG untuk spec berikutnya.

## Test Steps

### Pilihan page size (TC-FA-TAG-914)

1. Buka selector page size pada pagination tabel grup
2. Verifikasi opsi page size 10, 25, 50, 100
3. Verifikasi tidak ada opsi `All`
4. Verifikasi default terpilih 10
5. Tutup selector page size dengan Esc

### Navigasi halaman (TC-FA-TAG-915)

6. Klik halaman berikut
7. Verifikasi halaman 2 memuat baris ke-11 sampai ke-20
8. Klik halaman sebelumnya
9. Verifikasi halaman 1 memuat baris ke-1 sampai ke-10

### Ganti page size (TC-FA-TAG-916)

10. Pindah ke halaman 2
11. Ubah page size menjadi 25
12. Verifikasi tabel menampilkan halaman 1 dengan 25 baris
13. Ubah page size menjadi 10

### Input nomor halaman (TC-FA-TAG-917 sampai TC-FA-TAG-921)

14. Ketik `3` pada input nomor halaman lalu tekan Enter
15. Verifikasi tabel menampilkan halaman 3 (baris ke-21 sampai ke-25)
16. Pindah ke halaman 2 dengan klik halaman sebelumnya
17. Ganti isi input nomor halaman dengan `0`, tekan Enter
18. Verifikasi input diabaikan dan tabel tetap di halaman 2
19. Ganti isi input nomor halaman dengan `-1`, tekan Enter
20. Verifikasi input diabaikan dan tabel tetap di halaman 2
21. Ganti isi input nomor halaman dengan `4`, tekan Enter
22. Verifikasi input diabaikan dan tabel tetap di halaman 2
23. Ganti isi input nomor halaman dengan `abc`, tekan Enter
24. Verifikasi input diabaikan dan tabel tetap di halaman 2

## Notes

- Langkah penghubung (S-03): langkah 5 (menutup selector page size), 10 (TC-FA-TAG-916 langkah 1: pindah ke halaman 2), 13 (mengembalikan page size ke 10 supaya halaman 3 ada pada TC-FA-TAG-917), dan 16 (kembali ke halaman 2 untuk TC-FA-TAG-918 sampai TC-FA-TAG-921, yang semuanya berprecondition "berada di halaman 2").
- Langkah 12 hanya mengasersi jumlah baris pada halaman 1 (25 baris); tidak ada asersi lain atas halaman 3 pada page size 25.
- Dataset khusus 25 grup (precondition d TC-FA-TAG-914 s.d. TC-FA-TAG-921) berbeda dari dataset umum empat grup yang dipakai TC-FA-TAG-1, 928, 929, dan 1028; spec ini membentuknya di hook `before`, sehingga tidak ada langkah penggantian dataset.
- Temuan untuk QA:
  - Nilai 21 grup tambahan pada dataset khusus tidak ditentukan TC; asersi spec hanya memakai jumlah baris (25) dan nomor baris, bukan isi grup tambahan.
  - Urutan baris pada halaman 2 dan 3 tidak ditentukan TC; Expected hanya menyebut nomor baris, sehingga asersi memakai nomor baris pada urutan bawaan tabel.
  - Post Condition semua TC ("tidak ada perubahan data bisnis") tidak punya langkah observasi dan tidak diasersi.

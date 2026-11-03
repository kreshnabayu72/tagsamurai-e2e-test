---
id: TC-FA-LBL-E2E-004-pagination-labels-list-company-volume
title: "Pagination Labels List (Company Volume)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-17
  - TC-FA-LBL-278
  - TC-FA-LBL-279
  - TC-FA-LBL-280
coverage:
  web: automated
---

# Pagination Labels List (Company Volume)

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya.
- Akun aktor: Total Control `Company Volume` (Pre-setup #10, `Total Control Volume`), `Fixture.assetLabeling.akun.totalControlVolume`, `Spectra.env.FA_TC_VOLUME_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Environment variable: `FA_TC_VOLUME_PASSWORD`, `FA_LBL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Pre-setup (dibaca saja, tidak diubah spec): #10 `Company Volume` dengan 120 label `Project Tag 1` sampai `Project Tag 120`; N total = 120 label dari seeding Pre-setup. Selection Limit tidak diubah spec ini.
- Tabel "Page size TC-FA-LBL-278" (parameter pengulangan langkah 7 sampai 11):

| Page size |
|---|
| 25 |
| 50 |
| 100 |

- State global: tidak ada yang diubah selain sesi login. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-FA-LBL-17: Pagination Labels List: default 10 data per halaman dan pilihan page size

1. Verifikasi tabel menampilkan 10 baris pada halaman 1
2. Verifikasi info total 120 data
3. Buka pilihan page size
4. Verifikasi pilihan page size berisi `10`, `25`, `50`, `100`
5. Verifikasi tidak ada opsi `All` pada pilihan page size
6. Tutup pilihan page size dengan Esc

### TC-FA-LBL-278: Mengganti page size menjadi 25, 50, dan 100

7. Untuk setiap baris tabel "Page size TC-FA-LBL-278" (langkah 7 sampai 11): pindah ke halaman 2 pada page size yang sedang aktif
8. Ganti page size menjadi nilai kolom "Page size" baris itu
9. Verifikasi tabel menampilkan jumlah baris sama dengan nilai kolom "Page size" pada halaman 1
10. Verifikasi info total tetap 120 data
11. Verifikasi halaman 1 aktif
12. Ganti page size menjadi 10

### TC-FA-LBL-279: Navigasi halaman: berikutnya, sebelumnya, dan input nomor halaman

13. Klik halaman berikutnya
14. Verifikasi halaman 2 aktif
15. Klik halaman sebelumnya
16. Verifikasi halaman 1 aktif
17. Ketik `5` di input nomor halaman, tekan Enter
18. Verifikasi halaman 5 aktif

### TC-FA-LBL-280: Nomor halaman tidak valid diabaikan

19. Ketik `0` di input nomor halaman, tekan Enter
20. Verifikasi input `0` diabaikan dan tabel tetap di halaman 5
21. Ketik `999` di input nomor halaman, tekan Enter
22. Verifikasi input `999` diabaikan dan tabel tetap di halaman 5
23. Ketik `abc` di input nomor halaman, tekan Enter
24. Verifikasi input `abc` diabaikan dan tabel tetap di halaman 5

## Notes

- Langkah penghubung (S-03): langkah 6 (menutup pilihan page size), langkah 7 (pindah ke halaman 2 sebelum tiap penggantian page size supaya butir "selalu kembali ke halaman 1" pada Expected b TC-FA-LBL-278 bermakna, S-14), dan langkah 12 (mengembalikan page size ke 10 untuk TC berikutnya, S-09).
- Langkah berulang: langkah 7 sampai 11 diulang tiga kali (25, 50, 100) memakai parameter tabel "Page size TC-FA-LBL-278" (bagian 8b butir 7); jumlah langkah terhitung dengan ekspansi 34.
- Kelas e (Company Volume, 120 label): spec ini tidak mengubah Selection Limit (Bulk Action Bar dan Select All ada di spec lain).
- Temuan untuk QA:
  - TC-FA-LBL-280 Expected "tabel tetap di halaman sekarang" tidak menyebut nomor halaman; spec mengasersi halaman 5 sesuai urutan TC-FA-LBL-279 (langkah 17) yang mendahuluinya dalam spec ini.
  - TC-FA-LBL-278 Langkah tidak menyebut halaman awal sebelum mengganti page size; spec menambah pindah ke halaman 2 (langkah 7).

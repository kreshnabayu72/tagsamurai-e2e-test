---
id: TC-FA-LBL-E2E-005-retensi-state-labels-list-dan-pagination-changelog-company-volume
title: "Retensi State Labels List dan Pagination Changelog (Company Volume)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-18
  - TC-FA-LBL-19
  - TC-FA-LBL-20
  - TC-FA-LBL-324
coverage:
  web: automated
---

# Retensi State Labels List dan Pagination Changelog (Company Volume)

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya.
- Akun aktor: Total Control `Company Volume` (Pre-setup #10, `Total Control Volume`), `Fixture.assetLabeling.akun.totalControlVolume`, `Spectra.env.FA_TC_VOLUME_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Environment variable: `FA_TC_VOLUME_PASSWORD`, `FA_LBL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Pre-setup (dibaca saja, tidak diubah spec): #10 `Company Volume` dengan 120 label `Project Tag 1` sampai `Project Tag 120` beserta log Create (satu entri Create per label, sehingga sedikitnya 120 entri Changelog; dipakai TC-FA-LBL-324 untuk page size 100). Search `Project Tag 1` menghasilkan 32 baris (4 halaman pada page size 10), Search `Project Tag 2` menghasilkan 11 baris (2 halaman), keduanya diturunkan dari nama label Pre-setup.
- Tabel "Page size TC-FA-LBL-324" (parameter pengulangan langkah 32 sampai 33):

| Page size |
|---|
| 25 |
| 50 |
| 100 |

- State global: tidak ada yang diubah selain sesi login. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-FA-LBL-18: Refresh F5 mempertahankan Search, Sort, Filter ter-Apply, dan halaman aktif

1. Ketik Search `Project Tag 1`, tekan Enter
2. Klik header kolom `Label` sampai Descending
3. Pindah ke halaman 2
4. Catat baris yang tampil pada halaman 2
5. Tekan F5
6. Verifikasi keyword `Project Tag 1` tetap terisi di Search
7. Verifikasi kolom `Label` tetap Descending
8. Verifikasi halaman 2 aktif dengan page size 10
9. Verifikasi baris yang tampil sama dengan catatan langkah 4
10. Klik `(←)` pada kotak Search

### TC-FA-LBL-19: Pindah ke tab Asset Name lalu kembali ke Labels memulihkan state tabel Labels

11. Ketik Search `Project Tag 2`, tekan Enter
12. Pindah ke halaman 2 dengan page size 10
13. Catat baris yang tampil pada halaman 2
14. Klik Tab `Asset Name`
15. Klik Tab `Labels`
16. Verifikasi Search menampilkan keyword `Project Tag 2`
17. Verifikasi halaman 2 aktif
18. Verifikasi baris yang tampil sama dengan catatan langkah 13
19. Klik `(←)` pada kotak Search

### TC-FA-LBL-20: Klik ulang menu Settings pada sidebar mereset Search, Sort, Filter, dan paginasi Labels

20. Ketik Search `Project Tag 3`, tekan Enter
21. Klik header kolom `Total Asset` sampai Ascending
22. Klik menu `Settings` pada sidebar navigasi
23. Buka Asset Master > Labels lagi
24. Verifikasi Search kosong
25. Verifikasi tidak ada filter ter-Apply
26. Verifikasi sort kembali ke default kolom `Label` A-Z
27. Verifikasi halaman 1 aktif

### TC-FA-LBL-324: Pagination Changelog: default 10 dan pilihan page size

28. Klik icon Changelog di Table Tools
29. Verifikasi Modal Changelog menampilkan default 10 baris per halaman
30. Buka pilihan page size Modal Changelog
31. Verifikasi pilihan page size berisi `10`, `25`, `50`, `100`
32. Untuk setiap baris tabel "Page size TC-FA-LBL-324" (langkah 32 sampai 33): ganti page size menjadi nilai kolom "Page size" baris itu
33. Verifikasi tabel Modal Changelog menampilkan jumlah baris sama dengan nilai kolom "Page size" baris itu
34. Tutup Modal Changelog

## Notes

- Langkah penghubung (S-03): langkah 4 dan 13 (mencatat baris halaman 2 sebagai baseline untuk asersi "baris yang sama"), langkah 10 dan 19 (mengosongkan Search; S-09), langkah 34 (menutup modal).
- Langkah berulang: langkah 32 sampai 33 diulang tiga kali (25, 50, 100) memakai tabel "Page size TC-FA-LBL-324" (bagian 8b butir 7); jumlah langkah terhitung dengan ekspansi 37.
- Alasan di atas sekitar 35 langkah (37 langkah dengan ekspansi): seluruh blok memakai Company Volume yang sama (kelas e), akun yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Absence pada langkah 25 (tidak ada filter ter-Apply): tabel Labels List yang sudah termuat dan Search kosong pada langkah 24 menjadi anchor permukaan (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-LBL-20 menyebut mereset Filter pada judul dan Expected tetapi langkahnya tidak menerapkan Filter sebelum klik menu Settings; asersi "tidak ada filter ter-Apply" tidak menguji reset Filter (S-15).
  - TC-FA-LBL-18 menyebut "Filter ter-Apply" pada judul tetapi langkahnya hanya memakai Search, Sort, dan halaman; Filter tidak diuji (S-15).
  - TC-FA-LBL-324 tidak menyebut jumlah entri Changelog Company Volume; spec menurunkannya dari 120 entri Create pada Pre-setup #10.

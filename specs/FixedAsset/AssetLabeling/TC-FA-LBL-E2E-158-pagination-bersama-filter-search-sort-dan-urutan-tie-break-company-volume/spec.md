---
id: TC-FA-LBL-E2E-158-pagination-bersama-filter-search-sort-dan-urutan-tie-break-company-volume
title: "Pagination bersama Filter, Search, Sort, dan Urutan Tie-Break (Company Volume)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-239
  - TC-FA-LBL-248
  - TC-FA-LBL-282
  - TC-FA-LBL-283
coverage:
  web: automated
---

# Pagination bersama Filter, Search, Sort, dan Urutan Tie-Break (Company Volume)

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya.
- Akun aktor: Total Control `Company Volume` (Pre-setup #10, `Total Control Volume`), `Fixture.assetLabeling.akun.totalControlVolume`, `Spectra.env.FA_TC_VOLUME_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Environment variable: `FA_TC_VOLUME_PASSWORD`, `FA_LBL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Pre-setup (dibaca saja, tidak diubah spec): #10 `Company Volume` dengan 120 label `Project Tag 1` sampai `Project Tag 120`, seluruhnya bernilai Total Asset 0; N total = 120 label dari seeding Pre-setup, page size awal 10 sehingga 12 halaman.
- Tabel "Halaman TC-FA-LBL-248" (parameter pengulangan langkah 20):

| Halaman |
|---|
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |
| 6 |
| 7 |
| 8 |
| 9 |
| 10 |
| 11 |
| 12 |

- State global: tidak ada yang diubah selain sesi login. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-FA-LBL-239: Apply filter saat di halaman lebih dari 1 mereset ke halaman 1

1. Pindah ke halaman 2
2. Klik icon Filter di Table Tools
3. Isi `Total Asset` Max `0`
4. Klik `[Apply]`
5. Verifikasi tabel kembali ke halaman 1
6. Verifikasi sedikitnya satu baris tampil pada tabel
7. Verifikasi tabel menampilkan hasil filter `Total Asset` Max 0
8. Bersihkan filter yang ter-Apply

### TC-FA-LBL-283: Menjalankan Search di halaman lebih dari 1 mereset ke halaman 1

9. Pindah ke halaman 3
10. Ketik Search `Project Tag 1`, tekan Enter
11. Verifikasi tabel kembali ke halaman 1
12. Verifikasi sedikitnya satu baris tampil pada tabel
13. Verifikasi setiap baris tabel memuat `Project Tag 1` sebagai hasil search
14. Klik `(←)` pada kotak Search

### TC-FA-LBL-282: Mengganti sort mempertahankan nomor halaman

15. Pindah ke halaman 3
16. Klik header `Label` sekali
17. Verifikasi tabel tetap di halaman 3
18. Verifikasi baris halaman 3 mengikuti urutan dataset baru (indikator sort aktif pada header `Label`)

### TC-FA-LBL-248: Urutan baris bernilai sama deterministik antar halaman

19. Klik header `Total Asset` sekali
20. Untuk setiap baris tabel "Halaman TC-FA-LBL-248" (langkah 20): buka halaman itu lewat input nomor halaman dan catat 10 label pada halaman itu
21. Verifikasi seluruh 120 label bernilai Total Asset 0 muncul tepat sekali tanpa baris ganda atau terlewat antar halaman
22. Verifikasi urutan seluruh label pada catatan lintas halaman adalah Label A-Z

## Notes

- Langkah penghubung (S-03): langkah 8 (membersihkan filter sebelum TC berikutnya, S-09), dan langkah 14 (mengosongkan Search sebelum TC berikutnya).
- Langkah berulang: langkah 20 diulang 12 kali memakai tabel "Halaman TC-FA-LBL-248" (bagian 8b butir 7); jumlah langkah terhitung dengan ekspansi 33.
- Urutan TC: TC-FA-LBL-239 dan TC-FA-LBL-283 sebelum TC-FA-LBL-282 dan TC-FA-LBL-248 karena dua yang terakhir mengubah sort dan tidak dikembalikan (S-10).
- Asersi universal pada langkah 7 dan 13 didahului langkah 6 dan 12 sebagai pembanding "sedikitnya satu baris" (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-LBL-282 Expected "urutan dataset baru" tidak menyebut arah sort (Ascending atau Descending) maupun baris halaman 3; spec hanya mengasersi halaman 3 tetap aktif dan indikator sort aktif pada header `Label`.
  - TC-FA-LBL-239 tidak menyebut label tombol untuk membersihkan filter; langkah 8 ditulis sebagai langkah penghubung tanpa label tombol.
  - TC-FA-LBL-248 menyebut "urutan Label A-Z" tanpa menyatakan apakah urutan natural (`Project Tag 2` sebelum `Project Tag 10`) atau leksikal; spec mengasersi urutan A-Z yang sama dengan kolom Label pada TC-FA-LBL-9.

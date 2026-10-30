---
id: TC-GS-TAG-E2E-024-validasi-identifier-gps-preview-duplicate-in-file-dan-total-scanned
title: "Validasi Identifier GPS: Invalid Format, Daftar Preview, Duplicate in File, dan Total Scanned"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-TAG-66
  - TC-GS-TAG-67
  - TC-GS-TAG-68
  - TC-GS-TAG-337
coverage:
  web: automated
---

# Validasi Identifier GPS: Invalid Format, Daftar Preview, Duplicate in File, dan Total Scanned

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor utama: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi), `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; layar awal Global Settings > TAG > Tab All dibuka hook `beforeEach`. Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
- Stok resmi Admin Console Client A (Device Name `Teltonika FMB920`, SKU `SKU-GPS-01`, Brand `Teltonika`, Model/Type `FMB920`) di-seed idempotent oleh fixture BE di hook `before`: GPS `356938035643001` (DD-S1) Available; setelah TC-67 melakukan Submit, hook `after` menghapus tag `356938035643001` dari registri Client A dan mengembalikan stok DD-S1 ke Available lewat fixture BE (disediakan tim FE/BE). Akun Admin Console untuk seeding stok disediakan tim FE (S-13).
- Data identifier: `35693803564` (DD-N6, IMEI 11 digit), `35693803564380A` (DD-N7, IMEI 15 karakter mengandung huruf), `356938035643101` (DD-N1, tidak ada di stok resmi). Opsi mandiri (BYO) aktif; Template Self-Purchased kosong.
- State: TC-67 melakukan Submit Activation dan mengubah registri Client A (30 baris Seed Registri A menjadi 31 dan kuota GPS terpakai bertambah 1); dipulihkan di hook `after` walau spec gagal. Footer registri `Showing 1 - 10 of 31 TAGs` valid hanya pada Seed Registri A utuh (Q-4).
- Kemampuan teknis: entri manual GPS (input teks dan tombol `Add`; label dan placeholder kontrol menunggu desain, NC-11, selektor disediakan tim FE sesuai plan bagian 6) dan unggah berkas CSV/XLSX; tidak ada endpoint atau selektor yang dikarang spec ini.
- Suite serial (`parallel: false`); spec tidak bergantung pada hasil spec lain. Identifier TAG (EPC, IMEI, UID) tetap dan tidak dapat diberi sufiks `{runId}` (S-12), sehingga seeding bersifat idempotent: hook `before` mengembalikan data yang dipakai spec ini ke kondisi awal (Q-4).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya; lihat `suite.md` bagian Hook Guided Tooltip.
- Nilai data mengacu ke `fixtures/all-tags.json` (identitas saja, dibuat tahap script); tidak ada password di fixture.

## Test Steps

### Sesi 1

1. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`

### TC-GS-TAG-66: Identifier GPS 15 karakter mengandung huruf tidak lolos Preview

2. Masukkan `35693803564380A` lewat entri manual
3. Verifikasi entri `35693803564380A` tampil di daftar Preview di bawah tabel staging dengan badge `Invalid Format`
4. Verifikasi entri `35693803564380A` tidak masuk tabel staging
5. Verifikasi `Total Scanned: 0` (entri tidak dihitung)

### TC-GS-TAG-68: IMEI sama dua kali dalam satu batch

6. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643001` lalu `356938035643001` sekali lagi
7. Verifikasi tidak ada Toast `T-02` (`Error, TAG is already on the list.`)
8. Verifikasi satu baris `356938035643001` di staging dengan status `Official`
9. Verifikasi entri kedua tampil di daftar Preview dengan badge `Duplicate in File`
10. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

### Sesi 2

11. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`

### TC-GS-TAG-337: Total Scanned menghitung seluruh baris staging

12. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643001`
13. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101` (baris `Needs Info`)
14. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `35693803564` (format salah, badge Preview)
15. Verifikasi `Total Scanned: 2` (baris `Official` dan baris `Needs Info`; entri Preview `Invalid Format` tidak dihitung)
16. Klik `Remove` pada baris `Needs Info` `356938035643101`, lalu klik `Remove` pada dialog
17. Verifikasi `Total Scanned: 1`
18. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

### Sesi 3

19. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`

### TC-GS-TAG-67: Entri gagal Preview: daftar terpisah, dapat dihapus, tidak ikut Submit, hilang saat sesi ditutup

20. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `35693803564` (11 digit)
21. Verifikasi entri `35693803564` berbadge `Invalid Format` di daftar Preview
22. Verifikasi entri `35693803564` bukan bagian `Total Scanned` (`Total Scanned: 0`)
23. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643001`
24. Hapus entri Preview `35693803564`
25. Verifikasi entri Preview `35693803564` terhapus dari daftar Preview
26. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `35693803564` lagi
27. Klik `Submit`
28. Verifikasi dialog `Submit Activation` memuat hanya `356938035643001` (entri Preview tidak ikut)
29. Konfirmasi dialog `Submit Activation`
30. Tunggu aksi selesai
31. Klik item sidebar `TAG`
32. Verifikasi footer registri Tab All `Showing 1 - 10 of 31 TAGs` (tepat satu tag bertambah dari 30 baris Seed Registri A)
33. Ketik Search `356938035643001`, tekan Enter
34. Verifikasi baris `356938035643001` tampil di registri
35. Klik `(←)` pada kotak Search
36. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
37. Verifikasi daftar Preview kosong (sesi baru tidak memuat entri Preview sebelumnya)
38. Verifikasi tabel staging kosong
39. Kembali ke List: klik item sidebar `TAG` (staging kosong)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Kelas harness: fungsional (validasi identifier GPS); TC-67 melakukan Submit sehingga ditempatkan di sesi terakhir.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Alasan di atas sekitar 35 langkah: satu kelas harness (fungsional), satu dataset GPS, dan tiga sesi yang berdiri sendiri; TC-66/TC-68 dan TC-337 tidak berbagi baris dan tidak bergantung pada hasil Submit TC-67. Sesi dipisah karena TC-337 mensyaratkan Total Scanned yang tidak tercampur baris sesi 1, dan TC-67 mengubah registri sehingga ditaruh paling akhir (prinsip 5 bagian 3).
- Langkah penghubung (tanpa `Verifikasi`): langkah mulai sesi menggabungkan TC langkah 1 sampai 3; `Klik Remove ... pada dialog` pada TC-337 menjalankan TC langkah 8; `Tunggu aksi selesai` dan `Klik item sidebar TAG` menjalankan TC-67 langkah 9; Search `356938035643001` dan `(←)` adalah langkah penghubung untuk memeriksa hasil commit; `Kembali ke List` dengan `Leave` adalah langkah penghubung (S-03): sesi dengan baris staging dianggap dirty sehingga keluar halaman memunculkan dialog konfirmasi; definisi dirty dan teks dialog diuji di spec 036 (TC-183 sampai TC-185, TC-111 sampai TC-113) dan tidak diasersi di spec ini.
- Spec memuat blok yang tidak mengubah data (TC-66, TC-68, TC-337) dan satu blok pembuat data (TC-67, Submit): blok pembuat ditaruh di sesi terakhir dan pemulihan registri serta stok dilakukan di hook `after`; satu topik (validasi identifier GPS) dan satu dataset, sehingga tidak dipecah.
- Footer registri diasersi sebagai hitungan setelah Seed Registri A utuh (30 baris) plus satu tag hasil commit; ini bukan total log (S-12).
- Temuan untuk QA:
  - TC-67 Langkah 8 tidak menyebut label tombol konfirmasi dialog `Submit Activation` (diuji di spec 031); spec menulis "Konfirmasi dialog" tanpa label.
  - TC-67 Expected c ("Submit hanya meng-commit `356938035643001`") hanya dapat diamati lewat dialog dan hitungan registri; absence entri `35693803564` di registri tidak dapat diasersi lewat Search substring karena `35693803564` adalah prefiks `356938035643001`, sehingga spec memakai footer registri `of 31` sebagai pengganti (usulan QA: TC menyebut asersi absence eksplisit).
  - TC-68 Expected b menyatakan "bukan Toast T-02"; spec mengasersi toast itu tidak muncul segera setelah penambahan (langkah penambahan menjadi anchor).
  - TC-66 dan TC-67 mensyaratkan `Total Scanned` tanpa menyebut angka dasar; spec memakai `0` sesuai sesi kosong.

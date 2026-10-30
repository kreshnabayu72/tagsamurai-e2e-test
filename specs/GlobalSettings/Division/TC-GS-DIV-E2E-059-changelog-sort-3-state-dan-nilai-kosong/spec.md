---
id: TC-GS-DIV-E2E-059-changelog-sort-3-state-dan-nilai-kosong
title: "Modal Changelog: Sort 3-State dan Nilai Kosong pada Old/New Value"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-206
  - TC-GS-DIV-207
  - TC-GS-DIV-208
  - TC-GS-DIV-209
coverage:
  web: automated
---

# Modal Changelog: Sort 3-State dan Nilai Kosong pada Old/New Value

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > Division.
- Akun aksi lewat API (tidak login UI): Create+Read, Rina Marlina (`Rina M`), `createOnly_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_CREATE_PASSWORD`; Update+Read, Agus Wijaya (`Agus W`), `updateOnly_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_UPDATE_PASSWORD`; Delete+Read, Dewi Lestari (`Dewi L`), `deleteOnly_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_DELETE_PASSWORD`.
- Environment variable: `GS_TC_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Seeding (lewat API oleh akun Sari Dewi di hook `before`, urutan sebagai berikut):
  - Jaminan dua nilai Date berbeda (kolom Date Modal Changelog berketelitian menit, S-12): entri Create pertama dibuat lebih dulu (Create `Accounting {runId}-059` oleh Sari Dewi lewat API; seeding via API disediakan tim FE), lalu hook `before` menjeda sampai menit berganti (jeda maksimum 60 detik; pengecualian atas jeda pendek karena Date berketelitian menit, bagian hook dan bukan langkah `Tunggu N detik`), lalu seeding berikutnya (Population, Edit, dan seluruh entri lain) dibuat sehingga ada minimal dua entri Changelog dengan Date menit berbeda. Asersi urutan Date (langkah 4, 6, 8, 14, 20, 26, dan 32) memakai entri-entri tersebut.
  - Population D-02 oleh Sari Dewi (seeding Division lewat API, setara TC-GS-DIV-30): 26 Division dengan nama dan Code literal Accounting (`ACC`), Administration (`ADM`), Audit (`AUD`), Business Development (`BD`), Corporate Communication (`CCM`), Customer Service (`CSV`), Data Analytics (`DA`), Engineering (`ENG`), Facilities (`FAC`), General Affairs (`GA`), Information Technology (`IT`), Internal Control (`IC`), Logistics (`LOG`), Marketing (`MKT`), Procurement (`PRC`), Product Management (`PM`), Production (`PRD`), Quality Assurance (`QA`), Research and Development (`RND`), Risk Management (`RSK`), Sales (`SLS`), Security (`SEC`), Strategy (`STR`), Supply Chain (`SC`), Training (`TRN`), Warehouse (`WH`). Seed idempotent: nama yang sudah ada dilewati; cleanup hanya menghapus yang dibuat spec ini. Tiap Create mencatat entri Changelog Action Create oleh `Sari D` (Old Value `—`). Menghasilkan lebih dari 10 entri Create (Old Value `—`), cukup agar baris `—` berada di halaman terakhir (Changelog append-only, jumlah entri Create tidak berkurang).
  - Division milik spec oleh Sari Dewi lewat API (setara TC-GS-DIV-101 dan TC-GS-DIV-102): `Accounting {runId}-059` (Code `ACC-059`) dibuat lalu Name-nya diubah menjadi `Accounting and Tax {runId}-059`, dan `Procurement {runId}-059` (Code `PRC-059`) dibuat lalu Code-nya diubah menjadi `PROC-059` (entri Action Create, lalu Edit Field `Division Name` dan `Code`, oleh `Sari D`). Population D-02 tidak diedit. Menyediakan baris Old Value dan New Value bernilai.
  - Division `Log Mixed Div {runId}-059` dibuat oleh Rina Marlina (entri Create oleh `Rina M`), diubah namanya oleh Agus Wijaya menjadi `Log Mixed Div Renamed {runId}-059` (entri Edit oleh `Agus W`), lalu dihapus oleh Dewi Lestari (entri Delete oleh `Dewi L`). Menyediakan keempat nilai Modified By (`Sari D`, `Rina M`, `Agus W`, `Dewi L`) agar sort Modified By dapat dibedakan dari urutan yang rusak.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Division Population yang dibuat spec ini dan Division bersuffix `-059` (termasuk `Accounting and Tax {runId}-059`, `Procurement {runId}-059`; hook `before` juga menghapus sisa bersuffix `-059` dari run lama). Entri Changelog tidak bisa dihapus.
- Kapasitas: Master Data Count Limit environment automation cukup untuk Division Pre-setup (6), Population (26), dan Division milik spec ini (`Accounting and Tax {runId}-059`, `Procurement {runId}-059`, `Log Mixed Div {runId}-059`; disediakan tim FE).
- Kemampuan teknis: klik header kolom sort; pindah ke halaman terakhir lewat Pagination (nomor halaman terakhir).
- Precondition TC-GS-DIV-206, 207, 208, 209: login sebagai Total Control dan berada di Global Settings > User > Division; riwayat Changelog terisi (Modified By: `Sari D`, `Rina M`, `Agus W`, `Dewi L`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite serial (`parallel: false`) karena Population D-02 bernama literal dan dipakai bersama spec lain.
- State global yang dipulihkan: tidak ada (sort hanya state tampilan modal).

## Test Steps

### TC-GS-DIV-209: Kolom Actions (⋯) Modal Changelog tidak memiliki ikon sort

1. Klik icon Changelog di Table Tools
2. Verifikasi header kolom Actions (⋯) tidak memiliki ikon sort

### TC-GS-DIV-207: Sort 3-state kolom Date Modal Changelog

3. Klik header Date
4. Verifikasi Date Oldest First (tanggal tertua di atas)
5. Klik header Date
6. Verifikasi Date Newest First (tanggal terbaru di atas)
7. Klik header Date
8. Verifikasi kembali ke default Date terbaru di atas

### TC-GS-DIV-206: Sort 3-state kolom teks Action, Division Name, Field, dan Modified By

9. Klik header Action
10. Verifikasi Action ascending A-Z
11. Klik header Action
12. Verifikasi Action descending Z-A
13. Klik header Action
14. Verifikasi Action kembali ke default Date terbaru di atas
15. Klik header Division Name
16. Verifikasi Division Name ascending A-Z
17. Klik header Division Name
18. Verifikasi Division Name descending Z-A
19. Klik header Division Name
20. Verifikasi Division Name kembali ke default Date terbaru di atas
21. Klik header Field
22. Verifikasi Field ascending A-Z
23. Klik header Field
24. Verifikasi Field descending Z-A
25. Klik header Field
26. Verifikasi Field kembali ke default Date terbaru di atas
27. Klik header Modified By
28. Verifikasi Modified By ascending A-Z
29. Klik header Modified By
30. Verifikasi Modified By descending Z-A
31. Klik header Modified By
32. Verifikasi Modified By kembali ke default Date terbaru di atas

### TC-GS-DIV-208: Sort kolom Old Value dan New Value menempatkan nilai kosong di akhir saat ascending

33. Klik header Old Value sekali (ascending)
34. Pindah ke halaman terakhir pada Pagination
35. Verifikasi Old Value ascending: baris dengan Old Value `—` (Create) berada paling akhir
36. Pindah ke halaman 1 pada Pagination
37. Klik header New Value sekali (ascending)
38. Pindah ke halaman terakhir pada Pagination
39. Verifikasi New Value ascending: baris dengan New Value `—` (Delete) berada paling akhir

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-DIV-209, 207, 206, 208. Alasan: TC-GS-DIV-209 hanya mengamati header (screening lebih dulu, bagian 3 konvensi); TC-GS-DIV-207 dan 206 mengembalikan sort ke default pada klik ketiga sehingga TC berikutnya mulai dari default; TC-GS-DIV-208 terakhir karena berakhir di halaman terakhir. Modal Changelog dibuka sekali di langkah 1.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 36 (kembali ke halaman 1 sebelum sort berikutnya, karena sort Old Value meninggalkan halaman terakhir).
- Pada TC-GS-DIV-208 "paling akhir" diasersi sebagai baris terakhir pada halaman terakhir; Expected TC tidak menyebut halaman, sehingga langkah pindah ke halaman terakhir (S-14) ditambahkan sebelum `Verifikasi`.
- Pada TC-GS-DIV-206, `Verifikasi ... kembali ke default Date terbaru di atas` dibaca sebagai baris terurut Date descending (langkah 14, 20, 26, dan 32), sama dengan kondisi default TC-GS-DIV-190 (spec 053); urutan diasersi pada entri dengan Date menit berbeda dari seeding (Prerequisites).
- Spec melewati sekitar 35 langkah (39 langkah) karena TC-GS-DIV-206 menguji empat kolom, masing-masing tiga klik dan tiga `Verifikasi` (S-01); semua blok satu kelas harness (sort Modal Changelog), satu akun, satu dataset. Modal Changelog dibuka sekali dan blok-blok melanjutkan state yang sama; sort tiap kolom dikembalikan ke default pada klik ketiga sehingga blok berikutnya mulai dari urutan default.
- Temuan untuk QA:
  - TC-GS-DIV-206: "klik 3 kembali ke default Date terbaru di atas" tidak menyebut apakah ikon sort Date ikut kembali ke Newest First; spec hanya mengasersi urutan baris.
  - TC-GS-DIV-208: tidak menyebut halaman tempat "paling akhir" diamati; spec memakai halaman terakhir.
  - TC-GS-DIV-206: tidak menyebut nilai urutan Modified By (nama singkat `Sari D` atau nama lengkap); spec mengasersi urutan yang tampil.
  - TC-GS-DIV-206 dan 207: ketelitian Date Modal Changelog dianggap menit (S-12); entri seeding bisa memiliki Date yang sama, sehingga hook `before` menjamin minimal dua entri dengan Date menit berbeda sebelum urutan Date diasersi.

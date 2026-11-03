---
id: TC-AC-ACAL-E2E-010-kombinasi-search-filter-sort-pagination-dan-pemulihan-no-result
title: "Kombinasi Search, Filter, Sort, Pagination, dan Pemulihan dari No-result"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-118
  - TC-AC-ACAL-119
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, Pagination, dan Pemulihan dari No-result

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; kredensial `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Email akun memuat placeholder `{namaCompany}` seperti di Pre-setup TC (lihat Temuan untuk QA).
- Data Log yang di-seed di hook `before` (kemampuan seeding log disediakan tim FE/BE; lihat Temuan untuk QA):
  - Tab User Action: sedikitnya 30 entri dengan Object `Partner`, 15 di antaranya Action `Suspend` dan 15 Action `Reassign`, dengan Name bersuffix `{runId}-010` yang memuat sedikitnya dua nilai distinct (mis. `Partner A {runId}-010` dan `Partner B {runId}-010`) supaya sort Name bermakna (S-11). Search `Partner` dengan Filter Action `Suspend` dan `Reassign` memberi lebih dari 25 hasil sehingga halaman 2 ada pada 25 baris per halaman.
  - Tab Session: sedikitnya satu entri dengan Division `Finance` dan sedikitnya satu entri dengan Division selain `Finance` (data Pre-setup No 12 yang hanya dibaca sebagai precondition; tidak ada nama subjek yang diasersi, sehingga tanpa nama literal).
  - Seeding idempotent (dilewati bila sudah ada), tidak dihapus (audit trail permanen). Tidak ada total entri yang diasersi.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- State global: tidak ada yang diubah.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACAL-118: Kombinasi Search + Filter + Sort + Pagination

1. Klik tab "User Action"
2. Ketik Search `Partner`, tekan Enter
3. Klik icon Filter, pilih Action `Suspend` dan `Reassign`, klik `[Apply]`
4. Klik sort Name sekali (Name ↑)
5. Ganti Rows per page ke `25`
6. Verifikasi tab User Action: sedikitnya satu baris tampil
7. Verifikasi hasil adalah irisan Search dan Filter: setiap baris memuat `Partner` dan Action `Suspend` atau `Reassign`
8. Verifikasi baris terurut Name ↑ pada halaman yang tampil
9. Pindah ke halaman 2
10. Verifikasi kotak Search masih berisi `Partner`
11. Verifikasi Filter Action `Suspend` dan `Reassign` masih aktif
12. Verifikasi Sort Name ↑ masih aktif
13. Klik `(←)` pada kotak Search tab User Action
14. Verifikasi Filter Action `Suspend` dan `Reassign` masih berlaku
15. Verifikasi Sort Name ↑ masih berlaku
16. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
17. Verifikasi kotak Search kosong
18. Verifikasi Sort Name ↑ masih berlaku

### TC-AC-ACAL-119: Pemulihan dari No results saat satu saringan dilepas

19. Klik tab "Session"
20. Ketik Search `zzz`, tekan Enter
21. Klik icon Filter, pilih Division `Finance`, klik `[Apply]`
22. Verifikasi ilustrasi dengan Title `No results found` dan Description `Try adjusting your search or filter.` (anchor)
23. Kosongkan isi kotak search, tekan Enter
24. Verifikasi tabel menampilkan sedikitnya satu baris
25. Verifikasi tabel menampilkan baris dengan Division `Finance`

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-118, 119). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik tab "User Action" memenuhi precondition TC-118 "berada di tab User Action"; tab awal dari `beforeEach` suite adalah Session; S-03), langkah 19 (berpindah ke tab Session untuk TC-119; state tab User Action tidak dipulihkan karena spec berakhir di tab Session dan state tab itu dibuang oleh `beforeEach` suite pada spec berikutnya).
- TC-118 langkah 2 ("Pindah halaman") ditulis "Pindah ke halaman 2"; TC tidak menyebut nomor halaman. TC-118 langkah 4 "Clear Field Filter + Apply" ditulis klik `[Clear Field]` lalu klik `[Apply]` pada Filter Panel.
- Langkah "Verifikasi tabel menampilkan sedikitnya satu baris" pada TC-119 dan pada TC-118 adalah pembanding sebelum asersi universal (bagian 8b butir 2); Expected TC tidak memuatnya. Pada TC-119 empty state `No results found` menjadi anchor positif bahwa Search dan Filter sudah diproses.
- Temuan untuk QA:
  - TC-118 Expected a "terurut Name ↑" bergantung pada sedikitnya dua nilai Name distinct; Prerequisites menuliskan komposisi seed.
  - TC-118 langkah 2 dan Expected b tidak menyebut halaman tujuan; spec memakai halaman 2 (butuh lebih dari 25 hasil).
  - TC-119 hanya menyebut "Clear Search + Enter"; spec menulisnya "kosongkan isi kotak search, tekan Enter" menurut bagian 8b butir 9 (Filter Division `Finance` tetap aktif).
  - Mekanisme seeding entri log tidak didefinisikan di TC, PRD, atau LLD yang dibaca; kemampuan itu diminta dari tim FE/BE.
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD` (akun `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`), terdaftar di `.env.example` dan `spectra.config.ts`.

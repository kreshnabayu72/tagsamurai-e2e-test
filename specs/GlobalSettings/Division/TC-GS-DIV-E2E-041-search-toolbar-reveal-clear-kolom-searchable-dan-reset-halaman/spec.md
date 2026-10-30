---
id: TC-GS-DIV-E2E-041-search-toolbar-reveal-clear-kolom-searchable-dan-reset-halaman
title: "Search Toolbar Tabel Division: Reveal, Clear, Kolom Searchable, dan Reset Halaman"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-141
  - TC-GS-DIV-142
  - TC-GS-DIV-143
  - TC-GS-DIV-144
  - TC-GS-DIV-145
  - TC-GS-DIV-148
coverage:
  web: automated
---

# Search Toolbar Tabel Division: Reveal, Clear, Kolom Searchable, dan Reset Halaman

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Division.
- Akun: Total Control, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > Division dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Finance (FIN), Human Resources (HR), Legal (LGL), Operations (OPS), Compliance (CMP), Treasury (TRS).
- Data Dinamis: Population D-02 (26 Division, Name (Code)): Accounting (ACC); Administration (ADM); Audit (AUD); Business Development (BD); Corporate Communication (CCM); Customer Service (CSV); Data Analytics (DA); Engineering (ENG); Facilities (FAC); General Affairs (GA); Information Technology (IT); Internal Control (IC); Logistics (LOG); Marketing (MKT); Procurement (PRC); Product Management (PM); Production (PRD); Quality Assurance (QA); Research and Development (RND); Risk Management (RSK); Sales (SLS); Security (SEC); Strategy (STR); Supply Chain (SC); Training (TRN); Warehouse (WH). Di-seed idempotent lewat kemampuan seeding Division lewat API di hook `before` dengan Name dan Code literal (dilewati bila sudah ada), sehingga tabel memuat 32 baris (6 Pre-setup + 26 Population), halaman 1 berisi 10 baris dan total 4 halaman. Nama literal tanpa suffix karena asersi jumlah 32 baris dan hasil Search bergantung pada kumpulan nama ini (bagian 5 konvensi, S-12). Cleanup di hook `after` hanya menghapus Division Population yang dibuat spec ini lewat API, tanpa berasumsi seeding berhasil penuh.
- Data uji per TC: TC-GS-DIV-141 dan TC-GS-DIV-142 keyword `Fin`; TC-GS-DIV-144 keyword `ACCOUN`, `accounting`, `QA`, `qa`; TC-GS-DIV-145 teks tanggal Last Updated baris `Quality Assurance` (dibaca dari tabel; format mengikuti General Settings); TC-GS-DIV-148 halaman awal 3 dan keyword `a`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan: kotak Search dan halaman tabel dikembalikan ke default (Search kosong dan tertutup, halaman 1) di akhir spec; hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > Division.
- Suite berjalan serial (`parallel: false`): tabel harus memuat tepat 32 baris (Pre-setup + Population) saat spec mulai, sehingga spec lain tidak boleh meninggalkan Division di environment.
- Kemampuan teknis: mengarahkan kursor ke icon Search untuk membaca tooltip; membaca teks sel Last Updated; memeriksa fokus kursor pada input Search.

## Test Steps

### TC-GS-DIV-141: Search Toolbar: reveal, auto-focus, tooltip, icon clear, dan submit lewat Enter

1. Arahkan kursor ke icon Search
2. Verifikasi tooltip icon Search tampil
3. Klik icon Search
4. Verifikasi Search bar melebar
5. Verifikasi kursor auto-focus di input Search
6. Verifikasi placeholder `Search division name or code...`
7. Ketik `Fin` pada kotak Search
8. Verifikasi icon `(✕)` muncul di dalam input
9. Verifikasi tabel belum tersaring (32 baris: halaman 1 berisi 10 baris dan footer menampilkan 4 halaman)
10. Tekan Enter
11. Verifikasi tabel hanya menampilkan satu baris
12. Verifikasi Name baris tersebut `Finance`
13. Verifikasi Code baris tersebut `FIN`

### TC-GS-DIV-142: Search Toolbar: icon clear mengosongkan input tanpa mereset tabel hingga Enter

14. Klik icon `(✕)`
15. Verifikasi input Search kosong
16. Verifikasi Search bar tetap terbuka
17. Verifikasi kursor tetap fokus di input Search
18. Verifikasi tabel tetap menampilkan hasil search terakhir (hanya baris `Finance`)
19. Tekan Enter pada input kosong
20. Verifikasi tabel mereset ke seluruh data (32 baris, 4 halaman)

### TC-GS-DIV-143: Search Toolbar: icon panah kembali menutup search dan mereset tabel langsung

21. Isi Search dengan `Fin`, tekan Enter
22. Klik icon panah `(←)` di kiri toolbar
23. Verifikasi kotak pencarian menutup menjadi icon Search biasa
24. Verifikasi tabel langsung kembali menampilkan seluruh data tanpa menekan Enter (32 baris)
25. Klik icon Search
26. Verifikasi input Search kosong (keyword dikosongkan)

### TC-GS-DIV-144: Search per kolom searchable: Name dan Code (substring dan tanpa membedakan huruf besar kecil)

27. Ketik Search `ACCOUN`, tekan Enter
28. Verifikasi tabel menampilkan baris `Accounting`
29. Ganti isi kotak search dengan `accounting`, tekan Enter
30. Verifikasi tabel menampilkan baris `Accounting`
31. Ganti isi kotak search dengan `QA`, tekan Enter
32. Verifikasi tabel menampilkan baris `Quality Assurance` (Code `QA`)
33. Ganti isi kotak search dengan `qa`, tekan Enter
34. Verifikasi tabel menampilkan baris `Quality Assurance` (Code `QA`)

### TC-GS-DIV-145: Last Updated tidak dapat dicari lewat Search toolbar

35. Baca teks tanggal Last Updated pada baris `Quality Assurance` yang tampil
36. Ganti isi kotak search dengan teks tanggal Last Updated tersebut, tekan Enter
37. Verifikasi tabel menampilkan `No results found` (Last Updated bukan kolom searchable)

### TC-GS-DIV-148: Search dari halaman lebih dari 1 mereset ke halaman 1

38. Klik icon panah `(←)` untuk menutup Search dan mereset tabel
39. Pindah ke halaman 3 tabel
40. Ketik Search `a`, tekan Enter
41. Verifikasi tabel kembali ke halaman 1
42. Verifikasi sedikitnya satu baris hasil search tampil di halaman 1
43. Verifikasi baris halaman 1 hanya memuat Division yang Name atau Code-nya memuat `a` (hasil search)
44. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE. Dependensi TC-GS-DIV-30 (Population) dipenuhi spec ini lewat seeding di hook `before`, tanpa menumpang spec lain.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (141, 142, 143, 144, 145, 148) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, dari state TC sebelumnya): langkah 38 (menutup Search dan mereset tabel sebelum TC-GS-DIV-148), langkah 44 (menutup Search di akhir spec), dan langkah 25 (membuka kembali Search untuk TC-GS-DIV-144 sekaligus memungkinkan observasi bahwa keyword dikosongkan setelah `(←)` pada langkah 26, Expected a TC-GS-DIV-143). Langkah 35 membaca teks tanggal dari baris hasil TC-GS-DIV-144 (TC sumber hanya menyebut "salah satu baris").
- Asersi tambahan (konkretisasi Expected): langkah 9 ("tabel belum tersaring" TC-GS-DIV-141 c ditulis 32 baris, halaman 1 berisi 10 baris, 4 halaman), langkah 20 ("seluruh data" TC-GS-DIV-142 c ditulis 32 baris, 4 halaman), langkah 24 ("seluruh data" TC-GS-DIV-143 b ditulis 32 baris), semuanya turunan dari Population D-02 dan 6 Pre-setup; langkah 43 (baris halaman 1 hanya memuat Division yang Name atau Code-nya memuat `a`, didahului anchor langkah 42: sedikitnya satu baris hasil tampil) adalah konkretisasi "dengan hasil search" pada Expected TC-GS-DIV-148.
- Search bar yang masih terbuka dari TC sebelumnya dipakai ulang: langkah 1 TC-GS-DIV-142 (cari `Fin` lalu Enter) dipenuhi state akhir TC-GS-DIV-141; langkah 21 (TC-GS-DIV-143, screening siklus input Search) memakai "Isi Search dengan" karena Search bar sudah terbuka dan input kosong, langkah 27 dan 40 memakai langkah atomik "Ketik Search" (membuka input bila tertutup), dan langkah 29, 31, 33, serta 36 memakai "ganti isi kotak search dengan" karena input masih berisi (bagian 8b butir 9).
- Pembagian TC lintas spec: TC-GS-DIV-146 dan TC-GS-DIV-147 (Search terhadap kolom hidden) ada di spec 048; TC-GS-DIV-149, 150, 152, 169 (Filter Panel) ada di spec 042; TC-GS-DIV-153 sampai 159 (kombinasi) ada di spec 043.
- Spec melewati sekitar 35 langkah (44 langkah) karena enam TC Search berbagi satu dataset 32 baris, satu layar, dan satu kelas harness (fungsional). Blok saling melanjutkan state: Search bar yang masih terbuka dari TC sebelumnya dipakai TC berikutnya (TC-GS-DIV-142 dari state akhir TC-GS-DIV-141, TC-GS-DIV-145 dari baris hasil TC-GS-DIV-144); memisahkannya mengulang login, seeding Population, dan pembentukan state Search yang sama.
- Temuan untuk QA:
  - TC-GS-DIV-141: teks tooltip icon Search tidak disebut di TC maupun PRD; spec hanya mengasersi tooltip tampil.
  - TC-GS-DIV-145: TC tidak menyebut baris mana yang dibaca tanggalnya; spec membaca baris `Quality Assurance` hasil TC-GS-DIV-144. Fungsi Filter Last Updated diuji di spec 042.
  - TC-GS-DIV-144: seluruh Name di Population berawal huruf kapital, sehingga bagian "tanpa membedakan huruf besar kecil" hanya teramati lewat keyword huruf kecil (`accounting`, `qa`).
  - TC-GS-DIV-143: ketika Filter aktif, TC tidak menyatakan apakah `(←)` juga mereset Filter; spec hanya menguji dengan Search saja.

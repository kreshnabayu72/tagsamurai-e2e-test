---
id: TC-AC-ACC-E2E-050-create-screening-opsi-partner-dan-select-group-tcp
title: "Popup New Client: Footer, Opsi Industry, Opsi Partner, Tree Select Group, dan Perilaku Partner-Group (Total Control)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-487
  - TC-AC-ACC-489
  - TC-AC-ACC-481
  - TC-AC-ACC-485
  - TC-AC-ACC-486
  - TC-AC-ACC-484
coverage:
  web: automated
---

# Popup New Client: Footer, Opsi Industry, Opsi Partner, Tree Select Group, dan Perilaku Partner-Group (Total Control)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (A-01) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login akun Total Control Principal di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Partner Suspended `CV Mitra Beku` (P-ROL-2, Tabel A3) tersedia dan tidak boleh muncul di opsi Partner. Partner aktif: CV Mitra Sejati, CV Mitra Lestari, CV Mitra Timur.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-050@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong.
- Dataset Dinamis: `PT Partner Dilepas {runId}-050` (submit diblokir, tidak dibuat), `PT Group Manual Lalu Partner {runId}-050` (dibuat).
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-487: Footer tetap terlihat saat body di-scroll

1. Klik `[+ New Client]`
2. Verifikasi footer memuat checkbox "Stay on this form after submitting", `[Clear Field]`, dan `[Submit]`
3. Scroll body popup sampai Section "Default User"
4. Verifikasi footer tetap terlihat di bagian bawah popup dengan ketiga elemen yang sama
5. Scroll body popup kembali ke atas
6. Verifikasi footer tetap terlihat

### TC-489: Dropdown Industry

7. Buka dropdown Industry
8. Verifikasi placeholder "Select industry" dan 15 opsi: Retail, Manufacturing, Logistics & Warehousing, Healthcare, Education, Finance & Banking, Technology, Construction, Hospitality, Government, Transportation, Telecommunications, Oil & Gas, Agriculture, Others
9. Ketik "Hosp" pada kotak pencarian dropdown
10. Verifikasi hanya "Hospitality" yang tersisa
11. Pilih opsi "Hospitality"
12. Verifikasi field Industry menampilkan "Hospitality"

### TC-481: Opsi Partner untuk Principal

13. Verifikasi field Partner menampilkan placeholder "Select partner(s) (optional)" dan tanpa pilihan
14. Buka dropdown Partner
15. Verifikasi opsi memuat CV Mitra Sejati, CV Mitra Lestari, dan CV Mitra Timur
16. Verifikasi "CV Mitra Beku" (Suspended) tidak ada di opsi

### TC-485: Partner dihapus memunculkan kembali Select Group wajib

17. Isi Company Name `PT Partner Dilepas {runId}-050`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Select Group dikosongkan
18. Pilih Partner "CV Mitra Sejati"
19. Verifikasi field Select Group tidak tampil
20. Hapus pilihan Partner "CV Mitra Sejati" hingga field Partner kosong
21. Verifikasi field Select Group tampil dengan placeholder "Select group" dan tanpa node terpilih
22. Klik `[Submit]`
23. Verifikasi pesan error inline di bawah Select Group: "Group must not be empty"
24. Verifikasi popup tetap terbuka
25. Verifikasi tidak ada toast sukses "Success, client has been created."

### TC-486: Partner dipilih setelah Group manual

26. Pilih Group "Cabang Menteng" pada tree Select Group
27. Ganti isi Company Name dengan `PT Group Manual Lalu Partner {runId}-050`
28. Pilih Partner "CV Mitra Sejati"
29. Verifikasi field Select Group tidak tampil
30. Klik `[Submit]`
31. Verifikasi toast sukses "Success, client has been created."
32. Ketik Search `PT Group Manual Lalu Partner {runId}-050`, tekan Enter
33. Verifikasi baris "PT Group Manual Lalu Partner {runId}-050": Managed By "CV Mitra Sejati"
34. Verifikasi baris "PT Group Manual Lalu Partner {runId}-050": Group "Area Jakarta" (Group Distributor induk, bukan "Cabang Menteng" yang dipilih manual)
35. Ketik Search `PT Partner Dilepas {runId}-050`, tekan Enter
36. Verifikasi tidak ada Client "PT Partner Dilepas {runId}-050" yang dibuat (empty state "No results found")

### TC-484: Tree Select Group untuk Total Control

37. Klik `[+ New Client]`
38. Biarkan Partner kosong dan lihat field Select Group
39. Verifikasi field Select Group menampilkan placeholder "Select group" dan tanpa node terpilih
40. Buka tree Select Group
41. Verifikasi tree memuat Regional Barat, Area Jakarta, Cabang Menteng, Cabang Bekasi, Cabang Kemang, Regional Timur, Area Surabaya, dan Cabang Rungkut, kedelapannya tampil normal (tidak greyed out dan tidak hidden)
42. Klik node "Area Surabaya"
43. Verifikasi "Area Surabaya" menjadi pilihan di field Select Group
44. Klik `[✕]` di header popup
45. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
46. Klik `[Leave]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (sekitar 46 langkah): satu role dan satu kelas (screening dan perilaku Partner-Group, tanpa data tercipta kecuali TC-486); tiap blok berdiri sendiri.
- Urutan (prinsip 6): satu popup dipakai untuk TC-487, TC-489, TC-481, TC-485, TC-486 (ditutup oleh submit sukses TC-486); popup kedua untuk TC-484, ditutup di akhir. Dua kali buka, dua kejadian menutup.
- Langkah penghubung (S-03): Search nama unik; penggantian Company Name sebelum TC-486; penutup form dirty (S-08). Verifikasi baris List TC-486 dilakukan sesudah popup tertutup karena List tertutup popup.
- Temuan untuk QA:
  - TC-485 data: Company Name `PT Partner Dilepas` dipakai untuk submit yang diblokir; TC-486 melanjutkan form yang sama dengan nama berbeda; keduanya tetap sesuai TC masing-masing.

---
id: TC-GS-UCF-E2E-021-form-user-tampilan-field-placeholder-required-dropdown-dan-date-picker
title: "Form User: Tampilan Custom Field (Placeholder, Tanda Required, Opsi Dropdown, Date Picker) dan Required Tidak Retroaktif"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-173
  - TC-GS-UCF-174
  - TC-GS-UCF-186
  - TC-GS-UCF-187
  - TC-GS-UCF-188
  - TC-GS-UCF-189
coverage:
  web: automated
---

# Form User: Tampilan Custom Field (Placeholder, Tanda Required, Opsi Dropdown, Date Picker) dan Required Tidak Retroaktif

## Prerequisites

- Mode: FE+BE (backend nyata). Cakupan lintas modul: field Custom Field pada form Create User (modul User) dan Edit User.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`; environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_<page_key>` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Layar awal: Global Settings > User > User List sub-tab Login User, dibuka di hook `beforeEach`.
- Data Pre-setup (di-seed lewat API di hook `before`, idempotent, fixture `Fixture.customFieldUser.preset14` (fixture baru, belum ada; lihat coverage); hanya dibaca, kecuali yang disebut di bawah): 14 Custom Field aktif Client A (D-01): 6 Pre-setup (`Cost Center` Dropdown `Finance`, `Operations`, `Marketing` dengan Placeholder `Select cost center` dan Required Yes; `Employee Grade` Text Required No; `Job Description`; `Bonus` Numeric Decimal Places 2; `Office Phone` Phone Required Yes; `Joining Date` [Inactive]) dan 8 Population (`Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID`, `Work Notes`, `Annual Target`, `badge number`). Hanya `Cost Center`, `Employee Grade`, `Bonus`, `Office Phone`, `Blood Type`, dan `Birth Date` yang dibaca langkah; field lain dipakai sebagai precondition TC (14 field aktif), tidak diasersi.
- Data Pre-setup user Client A: `Rahmat Hidayat` (Login User; dipakai langkah) dan `Intan Permata` (Login User; dipakai sebagai precondition TC-GS-UCF-188, `Retro Req` tanpa nilai, tidak diasersi). Last Name `Rahmat Hidayat` diubah oleh TC-GS-UCF-188 (Edit User) dan dipulihkan ke nilai semula lewat API di hook `after`; efek lain pada Pre-setup (Last Updated user itu) dicatat di Temuan untuk QA.
- Data dinamis (di-seed lewat API di hook `before` sebagai precondition; `{runId}` terdiri atas digit):
  - D-82 sampai D-84: `Ph Area {runId}-021` (Text Area, Placeholder `Write a short note`), `Ph Date {runId}-021` (Date, Placeholder `Pick a day`), `Ph Num {runId}-021` (Numeric, Placeholder `Enter amount`), `Ph Phone {runId}-021` (Phone, Placeholder `Contact number`); semuanya Active, Required No.
  - D-80: `Retro Req` (Text, Required No; `Rahmat Hidayat` dan `Intan Permata` tanpa nilai). Nama literal karena pesan error `Retro req must not be empty` diturunkan dari Field Name (pengecualian S-12 butir (ii)); seeding idempotent (dilewati bila sudah ada), hook `before` menghapus sisa `Retro Req` dari run lain, hook `after` menghapus yang dibuat spec ini.
  - Nilai yang hanya diketik: `abc` (Birth Date), `x` (Retro Req), Last Name hasil ubah `Hidayat {runId}-021`.
- Kondisi lain: Date Format Client A mengikuti General Settings (nilai format tidak disebut TC; tidak diubah spec ini). Field Required Yes lain di entitas Client A tidak ada selain `Cost Center`, `Office Phone`, dan `Tax ID` (dijamin hook `before` suite, butir D-158 di `suite.md`; spec ini tidak mengisi form hingga Submit).
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua field yang namanya memuat `{runId}-021` dan `Retro Req`; pulihkan Last Name `Rahmat Hidayat`.
- Kemampuan teknis: pembacaan placeholder dan tanda Required pada label form User; membuka dropdown dan date picker pada form User; menutup popup form User dirty lewat `[✕]` dan `[Leave]`; Search pada User List dan tabel Custom Field.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UCF-173: Form User menampilkan placeholder efektif tiap Custom Field aktif

1. Klik [+ User] pada tab User List sub-tab Login User
2. Verifikasi placeholder Employee Grade adalah `Enter employee grade`
3. Verifikasi placeholder Cost Center adalah `Select cost center` (Placeholder custom)
4. Verifikasi placeholder Bonus adalah `Enter bonus`
5. Verifikasi placeholder Office Phone adalah `Enter phone number`
6. Verifikasi placeholder Blood Type adalah `Select blood type`

### TC-GS-UCF-189: Placeholder custom tampil di form User untuk Data Type Text Area, Date, Numeric, dan Phone

7. Verifikasi placeholder `Ph Area {runId}-021` adalah `Write a short note`
8. Verifikasi placeholder `Ph Date {runId}-021` adalah `Pick a day`
9. Verifikasi placeholder `Ph Num {runId}-021` adalah `Enter amount`
10. Verifikasi placeholder `Ph Phone {runId}-021` adalah `Contact number`

### TC-GS-UCF-174: Custom Field Required ditandai pada label di form User

11. Verifikasi label Cost Center dan Office Phone memuat tanda Required
12. Verifikasi label Employee Grade tidak memuat tanda Required

### TC-GS-UCF-186: Dropdown Custom Field memuat value sesuai definisi dan urutan penambahan

13. Buka dropdown Cost Center
14. Verifikasi opsi `Finance`, `Operations`, `Marketing` sesuai urutan penambahan
15. Verifikasi tidak ada opsi lain
16. Tutup dropdown Cost Center dengan Esc

### TC-GS-UCF-187: Custom Field Date memakai date picker dan format mengikuti General Settings

17. Klik field Birth Date
18. Verifikasi kalender date picker tunggal terbuka
19. Pilih tanggal dari kalender
20. Verifikasi tanggal terpilih tampil dengan Date Format General Settings
21. Ketik teks bebas `abc` di field Birth Date
22. Verifikasi teks bebas tidak dapat dimasukkan

### Tutup form User dirty

23. Klik `[✕]`
24. Verifikasi dialog `Unsaved Changes` tampil
25. Klik [Leave]

### TC-GS-UCF-188: Required yang baru aktif tidak retroaktif dan baru berlaku saat nilai field diedit

26. Buka Global Settings > User > tab Custom Field
27. Ketik Search `Retro Req`, tekan Enter
28. Klik `⋯` pada baris `Retro Req` > Edit
29. Ubah switch Required Field menjadi Yes
30. Klik [Save]
31. Verifikasi Save diterima tanpa dialog
32. Verifikasi kolom Required baris `Retro Req` adalah `Yes`
33. Klik `(←)` pada kotak Search
34. Buka Global Settings > User > User List sub-tab Login User
35. Ketik Search `Rahmat Hidayat`, tekan Enter
36. Klik `⋯` pada baris `Rahmat Hidayat` > Edit
37. Ubah Last Name menjadi `Hidayat {runId}-021` (tanpa menyentuh Retro Req)
38. Klik [Save]
39. Verifikasi Edit User tersimpan tanpa error inline `Retro req must not be empty`
40. Ganti isi kotak search dengan `Rahmat Hidayat {runId}-021`, tekan Enter
41. Klik `⋯` pada baris `Rahmat Hidayat {runId}-021` > Edit
42. Isi Retro Req `x`
43. Hapus isi Retro Req
44. Klik [Save]
45. Verifikasi error inline `Retro req must not be empty`
46. Klik `[✕]`
47. Verifikasi dialog `Unsaved Changes` tampil
48. Klik [Leave]

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Spec melewati sekitar 35 langkah (smell, bagian 3 prinsip 13 konvensi): 6 TC satu topik (tampilan Custom Field pada form User) dengan satu akun; setiap Expected bermajemuk dipecah satu `Verifikasi` per klausa (S-01) dan blok per TC tetap bermakna bila blok sebelumnya gagal.
- Subjudul memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 173, 189, 174, 186, 187 (satu pembukaan form Create User, hanya membaca), lalu 188 (mengubah data) di akhir. Urutan sumber 173, 174, 186, 187, 188, 189 berubah demi satu pembukaan form: TC-GS-UCF-189 dipindah ke blok placeholder yang sama dengan TC-GS-UCF-173; TC-GS-UCF-188 mengubah Required dan data Pre-setup user sehingga ditaruh paling akhir (bagian 3 prinsip 5).
- Satu pembukaan form Create User (langkah 1) untuk satu kejadian menutup form (langkah 23 sampai 25, `[✕]` dengan `[Leave]` karena form dirty setelah memilih tanggal); form Edit User pada TC-GS-UCF-188 dibuka dua kali dan ditutup lewat `[Save]` dan `[✕]` dengan `[Leave]`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 16 (menutup dropdown), langkah 23 sampai 25 dan 46 sampai 48 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08), langkah 26 dan 34 (pindah tab), langkah 27, 35, 40 (Search), langkah 33 (reset Search), langkah 28, 36, 41 (membuka Edit), serta pengisian form dan klik tombol sebagai bagian langkah TC. Langkah 37 mengubah Last Name sebagai pemicu dan dipulihkan di hook `after`.
- Asersi "tersimpan" TC-GS-UCF-188 (langkah 39) hanya menyatakan tidak ada error inline; TC tidak menyebut toast Edit User (lihat Temuan untuk QA).
- Temuan untuk QA:
  - TC-GS-UCF-188 mengedit user Pre-setup `Rahmat Hidayat` (Last Name) dan tidak memulihkannya. Spec memulihkan Last Name lewat API di hook `after` (S-06); Last Updated user itu tetap berubah dan tidak dapat dipulihkan.
  - TC-GS-UCF-188 tidak menyebut toast hasil Edit User (teks toast modul User tidak tertulis di TC ini dan tidak ditelusuri ke PRD User); asersi "tersimpan" ditulis tanpa teks toast.
  - TC-GS-UCF-187 menyebut Date Format General Settings tanpa menyebut nilai format Client A; asersi mengikuti format General Settings Client A yang berlaku.
  - TC-GS-UCF-173 dan 189 tidak menyebut apakah placeholder Dropdown (`Select cost center`) dan Phone (`Enter phone number`) berada pada kontrol Number; spec mengasersi placeholder pada field masing-masing.
  - Nama `Retro Req` literal (pengecualian S-12 butir (ii), nama penentu pesan error); bila hook gagal menghapus sisa dari run lain, TC-GS-UCF-188 bisa gagal karena nama terpakai.

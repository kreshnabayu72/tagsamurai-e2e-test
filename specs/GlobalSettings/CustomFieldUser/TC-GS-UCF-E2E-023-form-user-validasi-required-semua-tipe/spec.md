---
id: TC-GS-UCF-E2E-023-form-user-validasi-required-semua-tipe
title: "Form User: Validasi Custom Field Required Kosong Ditolak untuk Dropdown, Text, Text Area, Date, dan Numeric"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UCF-185
  - TC-GS-UCF-544
  - TC-GS-UCF-498
  - TC-GS-UCF-499
  - TC-GS-UCF-500
coverage:
  web: automated
---

# Form User: Validasi Custom Field Required Kosong Ditolak untuk Dropdown, Text, Text Area, Date, dan Numeric

## Prerequisites

- Mode: FE+BE (backend nyata). Cakupan lintas modul: field Custom Field pada form Create User (modul User). Spec tidak membuat data; Submit selalu diblokir.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`; environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_<page_key>` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Layar awal: Global Settings > User > User List sub-tab Login User, dibuka di hook `beforeEach`.
- Data Pre-setup (di-seed lewat API di hook `before`, idempotent, fixture `Fixture.customFieldUser.preset14` (fixture baru, belum ada; lihat coverage); hanya dibaca): 14 Custom Field aktif Client A (D-01): 6 Pre-setup (`Cost Center` Dropdown `Finance`, `Operations`, `Marketing`, Required Yes; `Employee Grade`; `Job Description`; `Bonus`; `Office Phone` Phone Required Yes; `Joining Date` [Inactive]) dan 8 Population (`Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID` Text Required Yes, `Work Notes`, `Annual Target`, `badge number`). Hanya `Cost Center`, `Office Phone`, dan `Tax ID` yang dibaca langkah; field lain dipakai sebagai precondition TC (14 field aktif), tidak diasersi.
- Data dinamis (di-seed lewat API di hook `before` sebagai precondition): `Req Area` (D-222, Text Area, Required Yes, Active), `Req Date` (D-223, Date, Required Yes, Active), `Req Num` (D-224, Numeric, Required Yes, Active). Nama literal karena pesan error (`Req area must not be empty`, dst.) diturunkan dari Field Name (pengecualian S-12 butir (ii)); seeding idempotent (dilewati bila sudah ada), hook `before` menghapus sisa field bernama sama dari run lain, hook `after` menghapus yang dibuat spec ini.
- Kondisi D-158 (precondition TC): Custom Field Required Yes yang Active di Client A hanya `Cost Center`, `Office Phone`, `Tax ID`, serta `Req Area`, `Req Date`, `Req Num` (milik spec ini, di-seed hook `before` spec); selain keenam field itu, kondisi dijamin oleh hook `before` suite (butir D-158 di `suite.md`: Custom Field Required Yes Active lain dinonaktifkan atau dihapus lewat API dan dipulihkan di hook `after` suite; mekanisme disediakan tim FE/BE); spec ini tidak mengubah status field. Keenam field Required diisi seluruhnya kecuali satu field yang diuji pada tiap TC; ini menggabungkan precondition tiga TC (498 sampai 500) yang di TC berdiri sendiri-sendiri.
- Field wajib Create User (fixture form, tabel Data Uji Pre-setup TC): First Name `Probe`, Last Name `Custom`, Email `probeCustom<n>_automated_qaTeam1+{runId}-023@qwertysystem.net` (n = nomor TC; `{runId}` terdiri atas digit), Division = Division Client A mana pun (fixture modul Division, disediakan tim FE), Access = opsi pertama yang tersedia untuk Client A; field User opsional dikosongkan.
- Nilai yang hanya diketik: Cost Center `Finance`, Office Phone Country Code `🇮🇩 +62` dengan Number `81234567890`, Tax ID `TX-001`, Req Area `Note`, Req Date (tanggal dipilih dari kalender), Req Num `1`.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API `Req Area`, `Req Date`, `Req Num` yang dibuat spec; tidak ada user yang dibuat.
- Kemampuan teknis: mengosongkan input teks pada form User; memilih tanggal dari date picker; menutup popup Create User dirty lewat `[✕]` dan `[Leave]`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### Sesi form 1: Cost Center, Tax ID, Req Area, dan Req Num

1. Klik [+ User] pada tab User List sub-tab Login User
2. Isi Field wajib Create User (Email `probeCustom185_automated_qaTeam1+{runId}-023@qwertysystem.net`)
3. Isi Office Phone Country Code `🇮🇩 +62` dengan Number `81234567890`, Tax ID `TX-001`, Req Area `Note`, Req Date (pilih tanggal dari kalender), dan Req Num `1`; biarkan Cost Center belum dipilih

#### TC-GS-UCF-185: Custom Field Required kosong ditolak saat Submit

4. Klik [Submit]
5. Verifikasi error inline `Cost center must not be empty` pada Cost Center
6. Verifikasi User tidak tersimpan: popup Create User tetap terbuka tanpa toast sukses

#### TC-GS-UCF-544: Field Required berakronim menampilkan error dengan token akronim tetap kapital

7. Pilih Cost Center `Finance`
8. Kosongkan Tax ID
9. Klik [Submit]
10. Verifikasi error inline `Tax ID must not be empty` pada Tax ID (token `ID` tetap kapital dan huruf pertama pesan kapital)
11. Verifikasi User tidak tersimpan: popup Create User tetap terbuka tanpa toast sukses

#### TC-GS-UCF-498: Custom Field Required bertipe Text Area kosong ditolak saat Submit

12. Isi Tax ID `TX-001`
13. Kosongkan Req Area
14. Klik [Submit]
15. Verifikasi error inline `Req area must not be empty` pada Req Area
16. Verifikasi User tidak tersimpan: popup Create User tetap terbuka tanpa toast sukses

#### TC-GS-UCF-500: Custom Field Required bertipe Numeric kosong ditolak saat Submit

17. Isi Req Area `Note`
18. Kosongkan Req Num
19. Klik [Submit]
20. Verifikasi error inline `Req num must not be empty` pada Req Num
21. Verifikasi User tidak tersimpan: popup Create User tetap terbuka tanpa toast sukses
22. Klik `[✕]`
23. Verifikasi dialog `Unsaved Changes` tampil
24. Klik [Leave]

### Sesi form 2: Req Date

#### TC-GS-UCF-499: Custom Field Required bertipe Date kosong ditolak saat Submit

25. Klik [+ User] pada tab User List sub-tab Login User
26. Isi Field wajib Create User (Email `probeCustom499_automated_qaTeam1+{runId}-023@qwertysystem.net`)
27. Isi Cost Center `Finance`, Office Phone Country Code `🇮🇩 +62` dengan Number `81234567890`, Tax ID `TX-001`, Req Area `Note`, dan Req Num `1`; biarkan Req Date belum dipilih
28. Klik [Submit]
29. Verifikasi error inline `Req date must not be empty` pada Req Date
30. Verifikasi User tidak tersimpan: popup Create User tetap terbuka tanpa toast sukses
31. Klik `[✕]`
32. Verifikasi dialog `Unsaved Changes` tampil
33. Klik [Leave]

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 185, 544, 498, 500, 499 (urutan sumber 185, 544, 498, 499, 500). Dua sesi form: nilai dropdown dan tanggal yang sudah dipilih tidak dapat dikosongkan kembali, sehingga TC-GS-UCF-185 (Cost Center) berada di awal sesi 1 dan TC-GS-UCF-499 (Req Date) memakai sesi 2 yang dibuka bersih (prinsip 6 konvensi); TC teks (544, 498, 500) berurutan pada sesi 1 dengan mengosongkan satu input teks per kasus. Dua pembukaan form, dua kejadian menutup form (langkah 22 sampai 24 dan 31 sampai 33).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2, 3, 7, 8, 12, 13, 17, 18, 26, 27 (mengisi atau mengosongkan field sebagai persiapan TC), langkah 22 sampai 24 dan 31 sampai 33 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08).
- Precondition TC-GS-UCF-498 sampai 500 menyatakan field Required lain Inactive, sedangkan spec ini memelihara semuanya Active dan mengisinya; error yang diasersi tetap hanya milik satu field yang dibiarkan kosong. Alasan gabungan: satu topik (Required kosong pada form User), satu akun, dan satu dataset seeding.
- Temuan untuk QA:
  - Penggabungan precondition 498 sampai 500 (field Required Req Area, Req Date, Req Num sama-sama Active) menyimpang dari precondition tiap TC (hanya satu Req field Active per TC); asersi tiap TC tetap sama.
  - TC-GS-UCF-185 dan 544 tidak menyebut apakah error field lain (mis. Req Area, Req Date, Req Num) ikut tampil; spec mengisi seluruh field lain agar tidak ambigu.
  - Plan menyebut 14 field Pre-setup; tabel Pre-setup TC memuat 6 field dan 8 sisanya Population TC-GS-UCF-1; spec men-seed keempat belas lewat API.

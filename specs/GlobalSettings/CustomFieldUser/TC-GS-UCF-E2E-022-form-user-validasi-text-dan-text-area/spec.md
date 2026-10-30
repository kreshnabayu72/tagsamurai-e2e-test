---
id: TC-GS-UCF-E2E-022-form-user-validasi-text-dan-text-area
title: "Form User: Validasi Batas Karakter Nilai Custom Field Text (120) dan Text Area (360)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UCF-175
  - TC-GS-UCF-176
coverage:
  web: automated
---

# Form User: Validasi Batas Karakter Nilai Custom Field Text (120) dan Text Area (360)

## Prerequisites

- Mode: FE+BE (backend nyata). Cakupan lintas modul: field Custom Field pada form Create User (modul User). Spec tidak membuat data; Submit selalu diblokir.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`; environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_<page_key>` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Layar awal: Global Settings > User > User List sub-tab Login User, dibuka di hook `beforeEach`.
- Data Pre-setup (di-seed lewat API di hook `before`, idempotent, fixture `Fixture.customFieldUser.preset14` (fixture baru, belum ada; lihat coverage); hanya dibaca): 14 Custom Field aktif Client A (D-01): 6 Pre-setup (`Cost Center` Dropdown `Finance`, `Operations`, `Marketing`, Required Yes; `Employee Grade` Text; `Job Description` Text Area; `Bonus` Numeric Decimal Places 2; `Office Phone` Phone Required Yes; `Joining Date` [Inactive]) dan 8 Population (`Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID` Text Required Yes, `Work Notes`, `Annual Target`, `badge number`). Hanya `Cost Center`, `Employee Grade`, `Job Description`, `Office Phone`, dan `Tax ID` yang dibaca langkah; field lain dipakai sebagai precondition TC (14 field aktif), tidak diasersi.
- Kondisi D-158 (precondition TC-GS-UCF-175 dan 176): Custom Field Required Yes yang Active di Client A hanya `Cost Center`, `Office Phone`, dan `Tax ID`; dijamin oleh hook `before` suite (butir D-158 di `suite.md`: Custom Field Required Yes Active selain yang disebut dinonaktifkan atau dihapus lewat API sebelum spec berjalan dan dipulihkan di hook `after` suite; mekanisme disediakan tim FE/BE); spec ini tidak mengubah status field.
- Field wajib Create User (fixture form, tabel Data Uji Pre-setup TC): First Name `Probe`, Last Name `Custom`, Email `probeCustom<n>_automated_qaTeam1+{runId}-022@qwertysystem.net` (n = nomor TC; `{runId}` terdiri atas digit), Division = Division Client A mana pun (fixture modul Division, disediakan tim FE), Access = opsi pertama yang tersedia untuk Client A; field User opsional dikosongkan.
- Data dinamis: tidak ada yang tersimpan. Nilai yang hanya diketik: 120 dan 121 karakter `A` (Employee Grade), 360 dan 361 karakter `B` (Job Description), `Finance`, `81234567890`, `TX-001`.
- Cleanup: tidak ada data yang dibuat.
- Kemampuan teknis: mengetik nilai panjang pada input Custom Field di form User; menutup popup Create User dirty lewat `[✕]` dan `[Leave]`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### Persiapan form Create User

1. Klik [+ User] pada tab User List sub-tab Login User
2. Isi Field wajib Create User (Prerequisites) dan Custom Field Required: Cost Center `Finance`, Office Phone Country Code `🇮🇩 +62` dengan Number `81234567890`, Tax ID `TX-001`

### TC-GS-UCF-175: Nilai Text 120 karakter diterima dan 121 karakter menampilkan error

3. Ketik 120 karakter `A` di Employee Grade
4. Verifikasi tidak ada error pada Employee Grade
5. Tambahkan 1 karakter `A` (total 121 karakter)
6. Verifikasi error inline `Max. 120 characters` muncul real-time
7. Klik [Submit]
8. Verifikasi popup Create User tetap terbuka
9. Verifikasi error inline `Max. 120 characters` tetap tampil
10. Verifikasi tidak ada toast sukses
11. Kosongkan Employee Grade

### TC-GS-UCF-176: Nilai Text Area 360 karakter diterima dan 361 karakter menampilkan error

12. Ketik 360 karakter `B` di Job Description
13. Verifikasi tidak ada error pada Job Description
14. Tambahkan 1 karakter `B` (total 361 karakter)
15. Verifikasi error inline `Max. 360 characters` muncul real-time
16. Klik [Submit]
17. Verifikasi popup Create User tetap terbuka
18. Verifikasi error inline `Max. 360 characters` tetap tampil
19. Verifikasi tidak ada toast sukses

### Tutup form User dirty

20. Klik `[✕]`
21. Verifikasi dialog `Unsaved Changes` tampil
22. Klik [Leave]

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 175, 176 (sama dengan sumber). Satu pembukaan form Create User dipakai untuk kedua TC (kasus yang hanya mengetik dan Submit diblokir, prinsip 13 "halaman yang sama dipakai berulang"); satu kejadian menutup form (langkah 20 sampai 22).
- Langkah 2 mengisi field wajib Create User dan Custom Field Required satu kali untuk kedua TC (precondition TC, tidak diasersi). Langkah 11 mengosongkan Employee Grade agar Submit TC-GS-UCF-176 hanya diblokir oleh error Job Description. Langkah 20 sampai 22 menutup form dirty (`Verifikasi` dialog `Unsaved Changes` mengikuti S-08). Ketiganya langkah penghubung.
- Nilai 120 dan 360 karakter diketik tanpa suffix karena tidak pernah tersimpan.
- Temuan untuk QA:
  - TC-GS-UCF-175 dan 176 mensyaratkan kondisi D-158 ("seluruh Custom Field Required Yes selain ... berstatus Inactive") tanpa menyebut cara menyiapkannya; spec merujuk jaminan hook `before` suite (butir D-158 di `suite.md`), mekanismenya disediakan tim FE/BE.
  - Plan menyebut 14 field Pre-setup; tabel Pre-setup TC memuat 6 field dan 8 sisanya Population TC-GS-UCF-1; spec men-seed keempat belas lewat API.
  - Division dan Access pada fixture form ditulis "mana pun" dan "opsi pertama" di TC; spec mengikuti tanpa menetapkan nilai tertentu (fixture modul Division disediakan tim FE).

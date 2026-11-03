---
id: TC-FA-RP-E2E-239-tooltip-hover-truncation-dan-tampilan-baris-2
title: "Tooltip, hover, truncation, dan tampilan baris (2/2)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-783
  - TC-FA-RP-784
  - TC-FA-RP-785
  - TC-FA-RP-786
  - TC-FA-RP-972
coverage:
  web: automated
---

# Tooltip, hover, truncation, dan tampilan baris (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #1 (Default User Admin Utama), #18 (pohon group), #36 (Tab Total Control terisi), #38 (Tab Group Manager terisi, termasuk Cahyo Aji pada group `International Operations Distribution Center` di bawah `Head Office`). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: pengguna Total Control bernama 57 karakter (precondition TC-FA-RP-785), email bersuffix `+{runId}-239`.
- Kemampuan teknis: Hover elemen UI. Seeding satu pengguna Total Control bernama `Muhammad Abdurrahman Al-Fatih bin Sulaiman Hakim Prasetyo` (57 karakter, nama literal karena TC menentukan panjang; email bersuffix `+{runId}-239`) lewat seeding API di hook `before`; pengguna itu dihapus di hook `after`.
- State yang diubah dan pemulihannya: Pengguna 57 karakter dibuat spec ini dan dihapus di hook `after`; tidak ada Pre-setup yang diubah.
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-783: Badge Group lebih dari 25 karakter dipotong 12 huruf pertama + `..` + 12 huruf terakhir dengan hover path penuh

1. Klik Tab `Group Manager`
2. Verifikasi badge Group baris Cahyo Aji menampilkan `Internationa..ution Center`
3. Hover badge Group baris Cahyo Aji
4. Verifikasi hover menampilkan path penuh `Head Office > International Operations Distribution Center`

### TC-FA-RP-784: Badge Group sampai 25 karakter ditampilkan penuh

5. Verifikasi badge Group baris Kevin Susanto di `Data Center` menampilkan `Data Center` penuh
6. Verifikasi badge Group baris Kevin Susanto di `Data Center` tanpa tanda `..`

### TC-FA-RP-785: Nama user sangat panjang pada kolom Name tidak dipotong dan kolom melebar

7. Klik Tab `Total Control`
8. Hover nama pengguna `Muhammad Abdurrahman Al-Fatih bin Sulaiman Hakim Prasetyo` pada kolom Name
9. Verifikasi nama tampil utuh (wrap natural atau hug content)
10. Verifikasi nama tanpa tanda `..`
11. Verifikasi tidak ada tooltip pemotongan

### TC-FA-RP-786: Tinggi baris tabel konsisten: nilai kolom tunggal tidak wrap

12. Verifikasi sedikitnya satu baris tampil di Tab `Total Control`
13. Verifikasi sel Status tetap satu baris pada semua baris
14. Verifikasi sel Last Updated tetap satu baris pada semua baris
15. Verifikasi tinggi baris konsisten

### TC-FA-RP-972: Prioritas tooltip UI mengikuti urutan baku bila beberapa kondisi benar sekaligus

16. Klik Tab `System`
17. Buka Detail Role `Manage accounting`
18. Hover checkbox CRUD baris Admin Utama (Default User sekaligus Total Control)
19. Verifikasi tooltip `Default User cannot be modified.` tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 19 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 7, 16. Akun aktor pertama sudah login di hook `before` (S-07).
- Pengecekan TC-FA-RP-785 butir "tanpa tooltip pemotongan" didahului langkah hover pada nama (langkah penghubung) supaya tooltip yang tidak ada dapat diamati; hover itu menjadi anchor absence (butir 8b.2).
- Temuan untuk QA:
  - TC-FA-RP-785 precondition d menyebut satu pengguna Total Control bernama 57 karakter yang tidak ada di Pre-setup #36 (9 baris) dan emailnya tidak tertulis; spec membuatnya lewat seeding API dengan nama persis TC dan email bersuffix.
  - TC-FA-RP-785 dan TC-FA-RP-786 tidak menyebut cara membuktikan "satu baris" dan "tinggi konsisten"; spec menulis asersi sesuai kata TC dan cara ukur ditentukan di tahap script.
  - TC-FA-RP-783 Data Uji menyebut group `International Operations Distribution Center` (44 karakter) di bawah `Head Office`, sedangkan Pre-setup #18 tidak memuat group itu; Pre-setup #38 yang memuatnya.

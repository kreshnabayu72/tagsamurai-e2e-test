---
id: TC-AC-LCS-E2E-124-changelog-isi-entri-trial-field-1-sampai-4
title: "Isi Entri Changelog per Field Tab Trial Settings: Max Trial Duration, Max Trial Asset Quota, Concurrent User Quota, dan First Notification"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-439
  - TC-AC-LCS-440
  - TC-AC-LCS-441
  - TC-AC-LCS-442
coverage:
  web: automated
---

# Isi Entri Changelog per Field Tab Trial Settings: Max Trial Duration, Max Trial Asset Quota, Concurrent User Quota, dan First Notification

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Kemampuan teknis: pembacaan total entri pada footer modal Changelog sebagai baseline N0 sebelum aksi (audit trail permanen; N tidak dapat diturunkan dari seeding, bagian 8b butir 10; baseline dicatat per tab). Precondition TC "Changelog tab kosong" tidak diasersi sebagai angka absolut: spec mengasersi selisih terhadap baseline N0 (S-12). Konfigurasi tab yang diubah spec dipulihkan ke default oleh hook `beforeEach` dan `after` suite.
- Waktu: jam server dan jam browser sinkron; Date entri baru dibandingkan dengan waktu yang dicatat sesudah toast sukses Save dengan toleransi satu menit karena kolom Date berketelitian menit (S-12).
- Parameter field (diulang di langkah 5 sampai 13; nomor iterasi k = 1 sampai 4 menurut urutan baris):
  | Field | Old Value | New Value |
  |---|---|---|
  | Max Trial Duration | 30 | 31 |
  | Max Trial Asset Quota | 50 | 51 |
  | Max Trial Concurrent User Quota | 10 | 11 |
  | First Notification | 7 | 8 |
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-439, TC-AC-LCS-440, TC-AC-LCS-441, TC-AC-LCS-442: Save perubahan satu field Trial Settings mencatat satu entri Edit pada Changelog Trial Settings

1. Klik icon Changelog di pojok kanan atas panel tab Trial Settings
2. Catat total entri pada footer modal sebagai baseline N0 (tab Trial Settings)
3. Tutup modal dengan `[✕]`
4. Untuk setiap baris tabel "Parameter field" pada Prerequisites, lakukan langkah 5 sampai 13
5. Ubah field sesuai kolom `Field` dari nilai kolom `Old Value` menjadi nilai kolom `New Value`
6. Klik `[Save]`
7. Verifikasi toast sukses "Success, trial settings have been saved."
8. Catat waktu sesudah toast sukses sebagai waktu Save
9. Klik icon Changelog di pojok kanan atas panel tab Trial Settings
10. Verifikasi footer menunjukkan total entri baseline N0 ditambah k, dengan k nomor iterasi (tepat satu entri baru pada tiap iterasi)
11. Verifikasi baris 1: Date sesuai waktu Save (format `dd MMM yy`, 24 jam, toleransi satu menit), Action `Edit`, Field sesuai kolom `Field`, Old Value sesuai kolom `Old Value`, New Value sesuai kolom `New Value`, Modified By `Andi W`
12. Verifikasi tidak ada baris baru untuk field lain (hanya satu entri baru pada iterasi ini)
13. Tutup modal dengan `[✕]`

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` tidak dipakai karena seluruh TC berbentuk satu blok yang diulang per field.
- Langkah yang diulang per field: langkah 5 sampai 13 (4 field Trial Settings); parameter tiap iterasi ada di tabel "Parameter field" pada Prerequisites. Tiap `Verifikasi` tetap satu per klausa (S-01).
- Langkah penghubung: langkah 1 sampai 3 (membaca baseline N0 lalu menutup modal, S-12), pencatatan waktu Save, dan menutup modal pada akhir tiap iterasi.
- Field yang disimpan tiap iterasi berbeda dari iterasi sebelumnya, sehingga Old Value tiap field tetap nilai default (Pre-setup 7).
- Entri baru dicari di antara baris teratas urutan Newest First; urutan antar entri dengan cap waktu menit yang sama tidak diasersi karena TC tidak menyebutnya.
- Setelah ekspansi blok ulang spec ini melewati sekitar 35 langkah (di atas smell): 3 langkah baseline ditambah 4 iterasi x 9 langkah = 39 langkah. Alasan mempertahankan satu spec: empat blok identik dalam bentuk, satu kelas (isi entri Changelog hasil Save satu field tab Trial Settings), dan berdiri sendiri karena tiap iterasi mengubah field yang berbeda dengan total entri yang dihitung dari baseline yang sama.
- Temuan untuk QA:
  - Expected TC (footer `1–N of N` dengan N sama dengan jumlah entri baru) mengandaikan Changelog tab kosong; Changelog bersifat permanen sehingga spec mengasersi total entri sebagai baseline N0 ditambah jumlah entri baru (S-12) dan memeriksa entri baru di baris teratas urutan Newest First.
  - Post Condition TC berupa nilai field tersimpan tidak punya langkah observasi sendiri di TC dan tidak diasersi; entri Changelog yang tercatat diasersi lewat Expected.

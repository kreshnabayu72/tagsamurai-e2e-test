---
id: TC-GS-NLU-E2E-128-create-beruntun-dua-belas-data-lewat-stay-on-this-form
title: "Create beruntun: dua belas data lewat Stay on this form"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-99
coverage:
  web: automated
---

# Create beruntun: dua belas data lewat Stay on this form

## Prerequisites

- Mode: FE+BE (backend nyata; record hasil Create dan jumlah baris tabel dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9 dan 10, hanya dibaca): Division `Logistics`, Login User `Ahmad Fauzi` (pool Represented By).
- Data Dinamis milik spec (Tabel Data Uji Dinamis No. 2): First Name `Populasi`, Division `Logistics`, Represented By `Ahmad Fauzi`. `Populasi Satu` (Email `populasi01+{runId}-128@qwertysystem.net`) di-seed lewat API di hook `before` sebagai hasil TC-GS-NLU-98 (dependensi TC-GS-NLU-99; S-04). Sebelas data lain dibuat lewat UI di langkah 3 sampai 6 dengan parameter tabel berikut:

  | Last Name | Email |
  |---|---|
  | Dua | `populasi02+{runId}-128@qwertysystem.net` |
  | Tiga | `populasi03+{runId}-128@qwertysystem.net` |
  | Empat | `populasi04+{runId}-128@qwertysystem.net` |
  | Lima | `populasi05+{runId}-128@qwertysystem.net` |
  | Enam | `populasi06+{runId}-128@qwertysystem.net` |
  | Tujuh | `populasi07+{runId}-128@qwertysystem.net` |
  | Delapan | `populasi08+{runId}-128@qwertysystem.net` |
  | Sembilan | `populasi09+{runId}-128@qwertysystem.net` |
  | Sepuluh | `populasi10+{runId}-128@qwertysystem.net` |
  | Sebelas | `populasi11+{runId}-128@qwertysystem.net` |
  | Dua Belas | `populasi12+{runId}-128@qwertysystem.net` |

- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Non-Login User ber-Email `+{runId}-128` lewat API (mekanisme seeding dan penghapusan disediakan tim FE/BE).
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

1. Klik `[+ Non-Login User]`
2. Centang `Stay on this form after submitting`

Untuk setiap baris tabel `Last Name` dan `Email` di Prerequisites (langkah 3 sampai 6):

3. Isi First Name `Populasi`, Last Name dan Email dari baris tabel, lalu pilih Division `Logistics` dan Represented By `Ahmad Fauzi` lewat `[+ Select User]`, baris `Ahmad Fauzi`, `[Select]`
4. Klik `[Submit]`
5. Verifikasi toast sukses `Success, non-login user has been created.`
6. Verifikasi popup tetap terbuka

Sesudah baris terakhir:

7. Klik `✕`
8. Ketik Search `{runId}-128`, tekan Enter
9. Verifikasi jumlah total baris Populasi 12 (`Populasi Satu` hasil seeding ditambah sebelas baris dari langkah 3 sampai 6)
10. Verifikasi tabel mempunyai lebih dari 1 halaman (pagination default 10 baris per halaman)

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Langkah 3 sampai 6 diulang untuk setiap baris tabel Prerequisites (11 iterasi); parameter tiap iterasi hanya Last Name dan Email, tanpa langkah bersyarat (8b.7).
- Alasan di atas sekitar 35 langkah: dengan ekspansi 11 iterasi spec ini 2 + 11 x 4 + 4 = 50 langkah. Spec hanya memuat satu TC dan satu alur berulang yang sama (Create beruntun dengan `Stay on this form after submitting`); tiap iterasi identik kecuali Last Name dan Email, tidak ada blok berbeda yang dapat dipisah tanpa memutus asersi populasi akhir (langkah 9 dan 10).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 7 (menutup popup yang sudah kosong; sesuai langkah 4 TC sumber), langkah 8 (Search `{runId}-128` mencakup kolom Email supaya yang dihitung hanya data spec ini; R-16).
- Klausa Expected b TC-GS-NLU-99 ("Total minimal 12 baris Populasi") diasersi tepat 12 karena Search dibatasi pada data spec ini.
- Temuan untuk QA:
  - TC-GS-NLU-99 bergantung pada TC-GS-NLU-98 (`Populasi Satu`); spec men-seed `Populasi Satu` lewat API sehingga tidak bergantung pada hasil spec lain (S-06).
  - TC-GS-NLU-99 langkah 3 ("Ulangi isi dan `[Submit]`") tidak menyebut Last Name `Dua` s.d. `Dua Belas` secara rinci; spec memakai penamaan kata bilangan Indonesia dari Data Uji ("Populasi Dua s.d. Populasi Dua Belas").
  - Search menyaring kolom Email tidak disebut eksplisit di TC bagian ini (asumsi sama seperti spec Create lain).

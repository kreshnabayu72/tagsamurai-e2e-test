---
id: TC-AC-RP-E2E-120-deskripsi-role-detail-global-role
title: "Deskripsi Role Detail Global Role Mengikuti Katalog untuk Setiap Role"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-38
coverage:
  web: automated
---

# Deskripsi Role Detail Global Role Mengikuti Katalog untuk Setiap Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: Tabel Data Uji Pre-setup #11 (tree group Principal). Berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Tabel "Deskripsi Global Role" (parameter langkah berulang; teks persis kolom "Deskripsi UI (Sub-title Header)" katalog PRD §2.6 yang dirujuk TC; TC hanya mencontohkan `Manage language`):

  | Role | Deskripsi |
  |---|---|
  | `Manage device master data` | This role allows the user to manage device categories, device names, and hardware SKUs through the Device Master Data menu. |
  | `Manage group` | This role allows the user to manage organizational group hierarchies through the Group menu. |
  | `Manage hardware stock` | This role allows the user to manage hardware stock receipts and inventory through the Hardware Stock menu. |
  | `Manage language` | This role allows the user to manage supported languages and UI translations through the Language menu. |
  | `Manage plans & licensing` | This role allows the user to manage subscription plans, tier entitlements, and licensing packages through the Plans & Licensing menu. |
  | `Manage preload` | This role allows the user to manage system preload master data through the Preload menu. |
  | `Manage presetup` | This role allows the user to manage device presetup templates through the Presetup menu. |
  | `Manage privacy policy` | This role allows the user to view version history, edit content, and publish new versions of the platform Privacy Policy. |
  | `Manage TAG stock` | This role allows the user to manage physical TAG stocks through the TAG menu. |
  | `Manage user and role` | This role allows the user to manage user accounts and role permissions through the User and Role & Permission menus. |

- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis, seeding, atau suffix `{runId}`. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-38: Deskripsi Global Role mengikuti katalog untuk setiap role

1. Klik tab `System`
Untuk setiap baris tabel "Deskripsi Global Role" di Prerequisites (langkah 2 sampai 4, 10 iterasi):
2. Pada section Global Role, klik `⋯` pada baris role lalu klik `Detail`
3. Verifikasi deskripsi di bawah Title halaman Role Detail sama persis dengan kolom Deskripsi tabel untuk role itu
4. Klik segmen "System" pada Breadcrumb untuk kembali ke Tab System

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Seluruh TC spec ini TC FE; spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah berulang per baris tabel Prerequisites (8b butir 7): langkah 2 sampai 4 diulang 10 kali (satu per Global Role Principal); ekspansi 3 langkah x 10 iterasi ditambah 1 langkah pembuka berjumlah 31, di bawah batas sekitar 35 langkah. `Verifikasi` tetap satu per iterasi (satu klausa deskripsi, S-01).
- Langkah penghubung tanpa awalan Verifikasi (S-03): klik segmen "System" pada Breadcrumb (langkah 4) mengembalikan Tab System sebelum iterasi berikutnya.
- Pembagian TC lintas spec: TC-AC-RP-34 sampai TC-AC-RP-37 (screening Role Detail Global Role) ada di spec 009; verifikasi deskripsi `Manage device master data` juga ada di sana (langkah Page Header), sedangkan spec ini memeriksa sepuluh role.
- Temuan untuk QA:
  - TC-AC-RP-38 hanya mencontohkan teks deskripsi `Manage language` dan menunjuk kolom "Deskripsi UI (Sub-title Header)" katalog §2.6; teks sembilan role lain diambil dari PRD §2.6 (satu-satunya sumber teks), bukan dari TC. Perlu konfirmasi QA agar teks itu dimasukkan ke TC.
  - TC-AC-RP-38 menyebut "10 role"; spec memakai 10 Global Role entitas Principal sesuai TC-AC-RP-28.

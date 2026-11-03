---
id: TC-AC-RP-E2E-121-deskripsi-role-detail-group-role
title: "Deskripsi Role Detail Group Role Mengikuti Katalog untuk Setiap Role"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-50
coverage:
  web: automated
---

# Deskripsi Role Detail Group Role Mengikuti Katalog untuk Setiap Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: Tabel Data Uji Pre-setup #11 (tree group Principal). Berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Tabel "Deskripsi Group Role" (parameter langkah berulang; teks persis kolom "Deskripsi UI (Sub-title Header)" katalog PRD §2.7 yang dirujuk TC; TC hanya mencontohkan `Manage partner`):

  | Role | Deskripsi |
  |---|---|
  | `Manage active client` | This role allows the user to manage active client profiles and settings within assigned groups through the Active Client menu. |
  | `Manage allocation` | This role allows the user to manage device allocations, license allocations, and client subscriptions within assigned groups through the Allocation and Subscription menus. |
  | `Manage archived client` | This role allows the user to manage archived client records within assigned groups through the Archived Client menu. |
  | `Manage distributor` | This role allows the user to manage distributor organizations within assigned groups through the Distributor menu. |
  | `Manage partner` | This role allows the user to manage partner organizations within assigned groups through the Partner menu. |
  | `Manage wallet & pricing` | This role allows the user to manage wallet balances, top-up requests, and pricing settings within assigned groups through the Wallet and Pricing menus. |

- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis, seeding, atau suffix `{runId}`. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-50: Deskripsi Group Role mengikuti katalog untuk setiap role

1. Klik tab `System`
Untuk setiap baris tabel "Deskripsi Group Role" di Prerequisites (langkah 2 sampai 4, 6 iterasi):
2. Pada section Group Role, klik `⋯` pada baris role lalu klik `Detail`
3. Verifikasi deskripsi di bawah Title halaman Role Detail sama persis dengan kolom Deskripsi tabel untuk role itu
4. Klik segmen "System" pada Breadcrumb untuk kembali ke Tab System

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Seluruh TC spec ini TC FE; spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah berulang per baris tabel Prerequisites (8b butir 7): langkah 2 sampai 4 diulang 6 kali (satu per Group Role Principal); ekspansi 3 langkah x 6 iterasi ditambah 1 langkah pembuka berjumlah 19, di bawah batas sekitar 35 langkah. `Verifikasi` tetap satu per iterasi (satu klausa deskripsi, S-01).
- Langkah penghubung tanpa awalan Verifikasi (S-03): klik segmen "System" pada Breadcrumb (langkah 4) mengembalikan Tab System sebelum iterasi berikutnya.
- Pembagian TC lintas spec: TC-AC-RP-46 sampai TC-AC-RP-49 (screening Role Detail Group Role) ada di spec 012; verifikasi deskripsi `Manage distributor` juga ada di sana (langkah Page Header), sedangkan spec ini memeriksa enam role.
- Temuan untuk QA:
  - TC-AC-RP-50 hanya mencontohkan teks deskripsi `Manage partner` dan menunjuk kolom "Deskripsi UI (Sub-title Header)" katalog §2.7; teks lima role lain diambil dari PRD §2.7 (satu-satunya sumber teks), bukan dari TC. Perlu konfirmasi QA agar teks itu dimasukkan ke TC.

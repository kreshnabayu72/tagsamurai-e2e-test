---
id: TC-FA-PREF-E2E-029-gating-plan-starter-tab-preferences-tidak-terjangkau
title: "Gating Plan Starter: Entri Accounting Disabled dengan Chip Upgrade dan Tab Preferences Tidak Terjangkau"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-113
  - TC-FA-PREF-114
  - TC-FA-PREF-277
  - TC-FA-PREF-569
  - TC-FA-PREF-570
coverage:
  web: automated
---

# Gating Plan Starter: Entri Accounting Disabled dengan Chip Upgrade dan Tab Preferences Tidak Terjangkau

## Prerequisites

- Mode: FE+BE.
- Kelas harness: h (state tenant, plan). Spec hanya membaca state plan Starter; tidak mengubah plan.
- Akun aktor: Total Control tiap company plan Starter. Akun pertama: company PA-14. Login di hook `before` spec ini. Pengecualian layar awal: modul Accounting tidak terjangkau pada plan Starter, sehingga hook `beforeEach` suite hanya menutup dialog dan spec dimulai dari halaman beranda aplikasi. Ganti akun memakai langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Company dan akun:

  | Company | Plan | Total Control | TC |
  |---|---|---|---|
  | PA-14 | Starter, modul akuntansi dan Preferences tersimpan | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | TC-FA-PREF-113, TC-FA-PREF-114 |
  | PB-12 | Starter | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | TC-FA-PREF-277 |
  | PC-11 | Starter (sebelumnya Growth dengan Preferences terisi) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | TC-FA-PREF-569, TC-FA-PREF-570 |

  `{namaCompany}` ketiga company belum tertulis di TC; disediakan tim FE (lihat Temuan untuk QA). Password: `Spectra.env.FA_TC_PASSWORD`.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company plan Starter PA-14, PB-12, dan PC-11 hasil seed (butir "Seed dan pemulihan lewat API" di `suite.md`, disediakan tim FE/BE). Spec hanya membaca. URL langsung: Settings > Accounting > Preferences.
- State yang diubah spec: tidak ada.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-113: Company plan Starter melihat entri Accounting Disabled dengan chip Upgrade

1. Verifikasi entri sidebar Accounting Disabled dengan chip "Upgrade"
2. Verifikasi halaman Settings > Accounting dan tab Preferences tidak terjangkau lewat navigasi

### TC-FA-PREF-114: Akses langsung URL Preferences oleh Total Control pada plan Starter ditolak

3. Ketik atau tempel URL langsung Settings > Accounting > Preferences pada address bar lalu tekan Enter
4. Verifikasi permintaan Preferences ditolak server
5. Verifikasi sidebar menampilkan sedikitnya satu entri menu
6. Verifikasi form Preferences tidak ditampilkan
7. Verifikasi nilai Preferences tidak ditampilkan

### TC-FA-PREF-277: Entri Accounting Disabled dengan chip Upgrade untuk company PB-12

8. Logout dari akun Total Control company PA-14
9. Login sebagai Total Control company PB-12 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`)
10. Verifikasi entri sidebar Accounting Disabled dengan chip "Upgrade"
11. Verifikasi halaman Settings > Accounting dan tab Preferences tidak terjangkau lewat navigasi

### TC-FA-PREF-569: Entri Accounting Disabled dengan chip Upgrade untuk company PC-11

12. Logout dari akun Total Control company PB-12
13. Login sebagai Total Control company PC-11 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`)
14. Verifikasi entri sidebar Accounting Disabled dengan chip "Upgrade"
15. Verifikasi halaman Settings > Accounting dan tab Preferences tidak terjangkau lewat navigasi

### TC-FA-PREF-570: Membuka Preferences lewat URL langsung pada plan Starter tidak menampilkan form

16. Buka Settings > Accounting > Preferences lewat URL langsung
17. Verifikasi sidebar menampilkan sedikitnya satu entri menu
18. Verifikasi form Preferences tidak ditampilkan
19. Verifikasi nilai setting tidak ditampilkan

## Notes

- Kelas h (bagian 3 prinsip 13h): spec membaca state tenant (plan Starter) tanpa mengubah plan; perubahan plan ada di spec lain.
- Langkah penghubung (S-03): langkah 8, 9, 12, 13 (ganti akun). Langkah 5 dan 17 (sidebar menampilkan entri menu lain) adalah anchor positif asersi absence form dan nilai (8b.2) dan tidak ada di Expected TC.
- Asersi "tidak terjangkau lewat navigasi" (langkah 2, 11, 15) memakai entri sidebar Accounting Disabled (langkah sebelumnya) sebagai anchor permukaan.
- Temuan untuk QA:
  - Post Condition TC-FA-PREF-277 ("Nilai Preferences yang sudah tersimpan tetap sama dan tidak dihapus") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01).
  - Expected a TC-FA-PREF-114 ("Permintaan Preferences ditolak server") tidak menyebut status atau teks penolakan; spec mengasersi penolakan tanpa kode status.
  - Nama company dan email Total Control untuk PA-14, PB-12, dan PC-11 tidak tertulis di Pre-setup TC (hanya pola `{namaCompany}`); perlu dikonfirmasi tim FE.
  - TC-FA-PREF-113, 277, dan 569 menguji kondisi yang sama (plan Starter) pada tiga company seri fixture berbeda; tidak ada perbedaan asersi.

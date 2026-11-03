---
id: TC-AC-DC-E2E-025-defense-request-langsung-per-role-dan-entity
title: "Defense-in-Depth: Request Langsung per Role dan Entity Ditolak 403"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DC-244
  - TC-AC-DC-245
  - TC-AC-DC-246
  - TC-AC-DC-247
  - TC-AC-DC-248
  - TC-AC-DC-249
coverage:
  web: automated
---
# Defense-in-Depth: Request Langsung per Role dan Entity Ditolak 403

## Prerequisites

- Mode: FE+BE.
- Aktor: Create-Only (#4), Update-Only (#5), Delete-Only (#6), Read Only (#3), Distributor (#10), Partner (#11), dan Client (#12). Spec ini tidak membuka UI sebagai aktor-aktor itu: setiap aktor diwakili sesi API (token) yang dibuka di hook `before` spec ini; tiap blok TC memakai token aktornya tanpa ganti akun UI. Hook `after` mengembalikan sesi ke akun default suite.

| Role yang diuji | Akun (Pre-setup) | Password |
|---|---|---|
| Create-Only (Manage device master data: Create + Read) | #4 `manageDeviceC_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DC_CREATE_PASSWORD` |
| Update-Only (Manage device master data: Update + Read) | #5 `manageDeviceU_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DC_UPDATE_PASSWORD` |
| Delete-Only (Manage device master data: Delete + Read) | #6 `manageDeviceD_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DC_DELETE_PASSWORD` |
| Read Only (`Rina Wijaya`) | #3 `readOnlyDevCat_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DC_RO_PASSWORD` |
| Total Control entitas Distributor `Distributor Jaringan` | #10 `totalControlDistributor_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DC_DISTRIBUTOR_PASSWORD` |
| Total Control entitas Partner `Partner Jaringan` | #11 `totalControlPartner_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DC_PARTNER_PASSWORD` |
| Total Control entitas Client `Client Jaringan` | #12 `totalControlClient_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DC_CLIENT_PASSWORD` |

- Kemampuan teknis: sesi API aktor (login API password untuk akun yang sama dengan sesi UI, tidak dihitung sebagai sesi web) dan klien HTTP; disediakan tim BE/FE dan dinyatakan di `suite.md`.
- Data Dinamis (dibuat spec ini lewat API di hook `before` oleh Total Control #1, di bawah `Handheld Reader`): node `Pemindai Lintas {runId}-025` (leaf, target request update dan parent request create) dan `Pemindai Hapus {runId}-025` (leaf, target request delete). Nama yang dikirim di request: `Cross Edit {runId}-025`, `Cross Add Update {runId}-025`, `Cross Add Delete {runId}-025`, `Cross Edit Delete {runId}-025`, `Read Create {runId}-025`, `Read Edit {runId}-025`, `Distributor Create {runId}-025`, `Distributor Edit {runId}-025`.
- Data Pre-setup: #14 (Pohon Uji Kategori, hanya dibaca). Nilai data mengacu ke fixture `settingsDeviceCategory` (belum ada; disediakan tim FE). Nama node Pre-setup #14 ditulis sebagaimana di TC.
- Kemampuan membaca state pohon Category (nama dan keberadaan node) lewat fixture BE dan membaca jumlah entri Changelog Category (keduanya disediakan tim FE/BE); jumlah dicatat sebagai baseline di hook `before` sesudah seeding, dan asersi memakai perbandingan terhadap baseline itu.
- Hook `after`: menghapus semua node (dan Device Name) yang dibuat spec ini, termasuk node hasil aksi UI yang dikenali dari sufiks `{runId}-025`, lewat API dari anak ke induk; cleanup tidak berasumsi seeding berhasil penuh.
- Seeding dan cleanup menambah entri Changelog dan log audit permanen (Create dan Delete atas node bersufiks); entri itu tidak diasersi.
- Env var `AC_DC_CLIENT_PASSWORD`, `AC_DC_CREATE_PASSWORD`, `AC_DC_DELETE_PASSWORD`, `AC_DC_DISTRIBUTOR_PASSWORD`, `AC_DC_PARTNER_PASSWORD`, `AC_DC_RO_PASSWORD`, `AC_DC_UPDATE_PASSWORD` belum terdaftar: perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.
- Suite berjalan serial (`parallel: false`): pohon Category, Changelog, dan log audit adalah state bersama.

## Test Steps

### TC-AC-DC-244: Create-Only: request langsung update dan delete ditolak

1. Kirim request update nama `Pemindai Lintas {runId}-025` menjadi "Cross Edit {runId}-025" memakai token Create-Only
2. Kirim request delete `Pemindai Hapus {runId}-025` memakai token Create-Only
3. Verifikasi kedua request ditolak server dengan HTTP 403 karena capability Update dan Delete tidak dimiliki
4. Verifikasi (state data lewat fixture BE) nama `Pemindai Lintas {runId}-025` tidak berubah
5. Verifikasi (state data lewat fixture BE) `Pemindai Hapus {runId}-025` tetap ada
6. Verifikasi jumlah entri Changelog Category sama dengan baseline

### TC-AC-DC-245: Update-Only: request langsung create dan delete ditolak

7. Kirim request create Category "Cross Add Update {runId}-025" dengan parent `Pemindai Lintas {runId}-025` memakai token Update-Only
8. Kirim request delete `Pemindai Hapus {runId}-025` memakai token Update-Only
9. Verifikasi kedua request ditolak server dengan HTTP 403 karena capability Create dan Delete tidak dimiliki
10. Verifikasi (state data lewat fixture BE) `Pemindai Hapus {runId}-025` tetap ada
11. Verifikasi (state data lewat fixture BE) tidak ada node "Cross Add Update {runId}-025"
12. Verifikasi jumlah entri Changelog Category sama dengan baseline

### TC-AC-DC-246: Delete-Only: request langsung create dan update ditolak

13. Kirim request create Category "Cross Add Delete {runId}-025" dengan parent `Pemindai Lintas {runId}-025` memakai token Delete-Only
14. Kirim request update nama `Pemindai Lintas {runId}-025` menjadi "Cross Edit Delete {runId}-025" memakai token Delete-Only
15. Verifikasi kedua request ditolak server dengan HTTP 403 karena capability Create dan Update tidak dimiliki
16. Verifikasi (state data lewat fixture BE) nama `Pemindai Lintas {runId}-025` tidak berubah
17. Verifikasi (state data lewat fixture BE) tidak ada node "Cross Add Delete {runId}-025"
18. Verifikasi jumlah entri Changelog Category sama dengan baseline

### TC-AC-DC-247: Read Only: seluruh request mutasi langsung ditolak

19. Kirim request create (nama "Read Create {runId}-025", parent `Pemindai Lintas {runId}-025`) memakai token Read Only
20. Kirim request update (nama `Pemindai Lintas {runId}-025` menjadi "Read Edit {runId}-025") memakai token Read Only
21. Kirim request delete (`Pemindai Hapus {runId}-025`) memakai token Read Only
22. Verifikasi ketiga request ditolak server dengan HTTP 403
23. Verifikasi (state data lewat fixture BE) tree tidak berubah: `Pemindai Lintas {runId}-025` dan `Pemindai Hapus {runId}-025` tetap ada dengan nama semula dan tidak ada node "Read Create {runId}-025"
24. Verifikasi jumlah entri Changelog Category sama dengan baseline

### TC-AC-DC-248: Distributor: request mutasi langsung ditolak walau tree terlihat read-only

25. Kirim request create (nama "Distributor Create {runId}-025", parent `Pemindai Lintas {runId}-025`) memakai token Distributor `Distributor Jaringan`
26. Kirim request update (nama `Pemindai Lintas {runId}-025` menjadi "Distributor Edit {runId}-025") memakai token Distributor
27. Kirim request delete (`Pemindai Hapus {runId}-025`) memakai token Distributor
28. Verifikasi ketiga request ditolak server dengan HTTP 403
29. Verifikasi (state data lewat fixture BE) tree tidak berubah: `Pemindai Lintas {runId}-025` dan `Pemindai Hapus {runId}-025` tetap ada dengan nama semula dan tidak ada node "Distributor Create {runId}-025"
30. Verifikasi jumlah entri Changelog Category sama dengan baseline

### TC-AC-DC-249: Partner dan Client: request baca tree langsung ditolak

31. Kirim request baca tree Category memakai token Partner `Partner Jaringan`
32. Kirim request baca tree Category memakai token Client `Client Jaringan`
33. Verifikasi kedua request ditolak server dengan HTTP 403
34. Verifikasi kedua respons tidak mengembalikan data tree

## Notes

- Mode: FE+BE. K-1: Expected TC-AC-DC-244 sampai 249 berupa respons API (HTTP 403) dan state data; TC tetap di spec FE+BE walau tumpang tindih dengan `tc-settings-device-category-backend.md`. Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Request langsung dikirim lewat klien HTTP dengan token tiap aktor, tidak melewati browser (8b butir 1); asersi hanya status respons dan state data (fixture BE). Langkah TC "refresh halaman Device Name dan periksa tree" dan "Login sebagai Principal Total Control, refresh ..." (TC-AC-DC-248) dijalankan sebagai pemeriksaan state data lewat fixture BE; tampilan tree tidak diasersi di spec ini (8b butir 1).
- Enam blok TC kelas a independen dalam satu spec dengan satu baseline Changelog bersama; antar blok tidak ada langkah ganti akun UI karena token tiap aktor disediakan di hook `before`.
- Asersi "Changelog tidak bertambah" ditulis sebagai asersi jumlah dengan baseline (S-12), bukan asersi absence kelas g; TC-AC-DC-244 sampai 248 tidak punya spec absence yang memuat request ini.
- Anchor absence: keberadaan node milik spec dengan nama semula diasersi sebelum asersi "tidak ada node" pada TC-AC-DC-245 dan 246 (8b butir 2); pada TC-AC-DC-247 dan 248 klausa "tidak ada node" berada dalam satu asersi tree yang menyebut node pembanding.
- Temuan untuk QA:
  - Target aksi tulis dan hapus memakai node milik spec bersufiks `{runId}-025` (S-06, S-12); TC memakai node literal Pre-setup #14 (`Rugged Scanner` dan `Hapus Daun` pada TC-AC-DC-244 sampai 247, serta nama "Cross Edit" dan "Cross Add" pada Data Uji; nama pada request diberi sufiks `{runId}-025` dan dibedakan per blok) sebagai target. Hasil TC identik karena node milik spec adalah node user-created dengan perilaku yang sama; node literal Pre-setup hanya dibaca.
  - TC-AC-DC-247 dan 248 tidak menyebut nama atau parent request create, update, dan delete; spec memakai node milik spec dan nama bersufiks. TC-AC-DC-249 tidak menyebut endpoint baca tree; tidak dikarang (S-13).
  - TC-AC-DC-249 punya precondition login Total Control (UI) padahal Expected hanya respons API; token Partner dan Client diperoleh lewat sesi API aktor.
  - Mekanisme token tiap aktor, klien HTTP, dan pembacaan state lewat fixture BE disediakan tim BE/FE tanpa endpoint karangan.
  - Post Condition TC-AC-DC-244 sampai 249 ('-') tidak punya langkah observasi dan tidak diasersi.

# Spek Tidak Lolos karena BE, Belum Ada Issue di Gitea

Daftar spek e2e yang belum lolos (status gagal atau lolos tak lengkap) dengan penyebab di sisi BE, **dan belum punya issue di Gitea**. Dipakai untuk menentukan penyebab mana yang perlu dibuatkan issue atau dikirim ke BE. Spek di dalam dan di luar filter ikut didaftar.

## Cara membaca

- **Sumber:** laporan e2e (`/api/causes`, `/api/specs` dengan `scope=all`, `/api/refs`, `/api/be-issues`), diambil 2026-11-19, dicocokkan dengan Gitea BETS-V2.
- **Kategori gap** (dari laporan):
  - **Bug BE:** bug nyata di API yang sudah ada (`be-bug`).
  - **Fitur BE belum ada:** endpoint atau kontrak belum dibangun (`feature-gap:be`).
  - **Helper atau seed dari BE:** butuh route atau seed khusus test dari BE (`helper-gap:be`).
  - **Gagal saat run, belum ada temuan BT:** spek gagal karena API menolak, tapi belum diklasifikasi dan belum punya catatan temuan.
- **BT** adalah ID baris temuan BE di laporan. Satu BT bisa menahan banyak spek, jadi tabel dikelompokkan per BT.
- **Draf:** nama file draf issue bila sudah ada tapi belum diposting ke Gitea.
- **Tidak termasuk:**
  - penyebab yang sudah punya issue di Gitea, terbuka, closed, atau hold (67 baris spek);
  - penyebab yang teksnya menyebut nomor issue Gitea (268 baris spek);
  - spek yang sudah ada di daftar urutan pengerjaan issue BE (11 baris spek).
- Satu spek bisa punya lebih dari satu penyebab, sehingga muncul di beberapa BT. Jumlah "spek unik" menghitungnya sekali.

## Hasil verifikasi (19 Nov)

Tiap entri di bawah sekarang punya baris **Verifikasi**. Dicek ke laporan e2e, Gitea, `plans/_program/be-filing/drafts/`, sprint board 19 Nov, dan `spec-decisions.md`. Jumlah entri di sini 142 (Gagal saat run dihitung per spek di tabelnya).

| Verifikasi | Entri | Spek unik | Bug / Fitur / Helper |
|---|---|---|---|
| Perlu draf issue | 11 | 31 | 2 / 2 / 7 |
| Draf ada, menunggu "go" owner | 11 | 90 | 5 / 1 / 5 |
| Issue/helper sudah ada | 8 | 12 | 1 / 0 / 7 |
| Basi atau sudah selesai | 24 | 23 | 0 / 3 / 21 |
| Bukan BE | 25 | 36 | 0 / 6 / 19 |
| Kebutuhan BE nyata, belum ada ID BT | 47 | 37 | 0 / 2 / 45 |
| Ditahan / perlu baris BT atau bukti | 7 | 9 | 2 / 0 / 5 |
| Luar filter | 9 | 7 | 0 / 1 / 8 |

Koreksi atas isi awal dokumen:

- Entri yang sebenarnya **sudah punya issue**: BT-AC-DC-3 (`analytics-reporting-service#40`, closed; perlu dibuka ulang dengan nomor run), BT-AUTH-SES-1 (`iam-service#238`), BT-GS-UOM-2 (`enterprise-management-service#73`), entri `status/bulk` (`iam-service#184`), TAG Stock (`hardware-tagging-service#79`, `#128`).
- Entri **basi**: BT-114 (backend Import sudah ada), BT-GAP-37 (API License Allocation sudah ada, `enterprise-management-service#317`/`#318`), Hardware Stock "no backend" (sprint board baris 40 ⚙️), BT-GS-GSET-5 (ditutup D-270), BT-GS-HHR-3 (helper sudah diperbaiki), dan semua entri File Manager "Helpers now exist" (helper sudah ada, skrip belum memakainya).
- Entri **bukan BE**: sprint-gap (My Profile, Group Detail > Tab Assets, Pricing, Supply), keputusan owner (BT-6, BT-13), pemilik fe (BT-22), library TestSpectra (matcher `expiresAt`), aturan run (Principal tunggal, retensi platform), slice yang masih mock (All Tags).
- BT-GAP-16 Device Allocation: alasan tahan "out of sprint" sudah tidak berlaku (sprint board baris 41 🍰).
- "Gagal saat run" (22 spek): tidak satu pun bug BE yang siap di-file. Satu kebutuhan helper (`/v2/iam/dev/time/age` 500 di LP-036); sisanya skrip atau di luar filter.

Tindak lanjut:

- **Owner:** "go" untuk draf yang sudah ada: `BT-GS-IMP-39`, `BT-AC-SU-9`, `BT-GS-IMP-40`, `BT-GS-IMP-42`, `BT-GS-ROLE-15`, `BT-GAP-16`, `BT-AC-HS-1`, `BT-GS-IMP-1`, `BT-AC-SG-6`, `BT-GS-TAG-12`.
- **Coordinator → backend:** tulis draf untuk entri "Perlu draf issue": `BT-AC-SG-7`, `BT-GS-IMP-41`, `BT-AC-ACC-32`, `BT-AC-DS-17`, `BT-GS-IMP-3`, `BT-AC-CS-13`, `BT-GS-IMP-2`, `BT-AC-ACC-28`, `BT-AC-ACC-37`, `BT-AC-CS-28`, `BT-GS-IMP-4`. BT-AC-ACC-32 dan BT-AC-DS-17 adalah contract drift untuk pemilik LLD. BT-AC-ACC-28 dan BT-AC-ACC-37 bisa digabung ke draf helper yang sudah ada. Arsipkan draf `ems-license-allocation-license-api-not-implemented.md` (BT-GAP-37). Buka ulang `analytics-reporting-service#40` dengan nomor run (BT-AC-DC-3).
- **Sesi ac:** tulis baris BT untuk BT-AC-ACC-38, ACC-39, ACC-40, BT-LA-1 dan kebutuhan iam/ems tanpa ID (daftar sesi, penghitung pre-auth, jeda sweep, alert mail, expiry tanpa perpanjang, status Expired, `/dev/time/age` LP-036); retag LA 010/040/053/073, TAG Stock dan Hardware Stock dari run terbaru.
- **Sesi gs:** satu BT file-manager untuk set Upload/Deleted Date, file besar, pemicu auto-purge dan injeksi gagal storage; pakai helper `Spectra.setUserProfilePicture` / `seedFileManagerFile({ userId })` di skrip File Manager; daftarkan BT-NEW-F2; retag BT-114 dari run terbaru.
- **Sesi fai:** spek SettingsGroups di "Gagal saat run" pakai `GET /v2/iam/user-custom-fields/dropdown` dan body dari kontrak.

## Ringkasan

| Kategori | Spek unik | Penyebab (BT) | Gagal | Lolos tak lengkap | Dalam filter | Luar filter |
|---|---|---|---|---|---|---|
| Bug BE | 11 | 10 | 0 | 11 | 11 | 0 |
| Fitur BE belum ada | 28 | 15 | 1 | 28 | 28 | 1 |
| Helper atau seed dari BE | 189 | 117 | 20 | 227 | 233 | 14 |
| Gagal saat run, belum ada temuan BT | 22 | 2 | 22 | 0 | 17 | 5 |
| **Total** | **246** | **144** | | | | |

Kolom Gagal, Lolos tak lengkap, Dalam filter, dan Luar filter menghitung baris (spek per penyebab), jadi spek dengan banyak penyebab terhitung lebih dari sekali.

## Bug BE (11 spek)


### BT-GS-IMP-39: the draft read keeps the row Duplicate after the system Brand is deleted: skipped (bug in an existing backend API, see its BT row) (2 spek)

**Verifikasi:** Draf ada, menunggu "go" owner. Draf `import-staging-read-does-not-persist-duplicate-and-pending-row-status-changes.md` (import-service), belum diposting.

Draf: `import-staging-read-does-not-persist-duplicate-and-pending-row-status-changes.md` (belum diposting)

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-IMPORT-E2E-087` | GlobalSettings / Import | Re-evaluasi status duplicate: baris pembanding dihapus atau diubah, rekaman sistem dihapus atau dib… | High / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-140` | GlobalSettings / Import | Late-binding referensi saat commit: Division dihapus, Position di-rename, Represented By berubah, r… | Critical / Negative | Dalam | Lolos tak lengkap |

### BT-AC-ACC-40: the second Resend answers 500 (unique violation on the active activation token): skipped (bug in an existing backend API, see its BT row) (1 spek)

**Verifikasi:** Ditahan / perlu baris BT atau bukti. Baris BT tidak ada di file temuan. Pembanding: `iam-service#251` (closed, resend saat token aktif masih ada). Sesi ac menulis baris BT dengan nomor run. Bila 500 muncul dari fix #251, cukup komentar di #251, bukan issue baru.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-ACC-E2E-128` | AdminConsole / Client | Resend Activation Email: Jumlah Email dan Log pada Dua Klik, Pembatalan Retry Otomatis, dan Pencata… | High / Edge | Dalam | Lolos tak lengkap |

### BT-AC-CS-12: A Client's Default User (isTotalControl true) gets moduleAccess.adminConsole.hasAccess: true from /v2/me/permissions, so the portal shows the Admin C… (1 spek)

**Verifikasi:** Ditahan / perlu baris BT atau bukti. Baris BT: "NOT PROVEN, held". Perlu bukti run dulu, belum siap di-file.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-CS-E2E-016` | AdminConsole / LicenseAllocationSubscription | Role Matrix: Akses Menu dan URL Langsung per Entitas | Critical / Positive | Dalam | Lolos tak lengkap |

### BT-AC-DC-3: POST /v2/analytics-reporting/change-logs/export (format: "csv") writes Date as dd/MM/yy HH:mm without the comma (09/11/26 13:54); (1 spek)

**Verifikasi:** Issue/helper sudah ada. Issue sudah ada: `analytics-reporting-service#40` (closed, CSV export menulis tanggal tanpa koma). Spek masih lolos tak lengkap, jadi #40 dibuka ulang dengan nomor run (aturan Backend). Format yang dituju: D-272 (format General Settings, dengan koma).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-DN-E2E-149` | AdminConsole / SettingsDeviceName | Modal Changelog Download: Isi Berkas (Sheet1 XLSX, BOM CSV, Hyphen, Format Date, Modified By Nama L… | High / Positive | Dalam | Lolos tak lengkap |

### BT-AC-SG-7: Total Member counts an Archived Client. (1 spek)

**Verifikasi:** Perlu draf issue. Belum ada issue dan draf (enterprise-management, Total Member). Settings > Group ada di sprint board (baris 23).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-SG-E2E-039` | AdminConsole / SettingsGroup | Delete Group Diblok karena Entitas Menempel (D-03): Langsung, Descendant, Archived, Partner, dan Di… | Critical / Negative | Dalam | Lolos tak lengkap |

### BT-AC-SU-9: users/list with sortOrder: -1 puts an empty Position / Employee ID last; (1 spek)

**Verifikasi:** Draf ada, menunggu "go" owner. Draf `iam-ac-user-list-empty-values-last-in-both-sort-directions.md`, belum diposting.

Draf: `iam-ac-user-list-empty-values-last-in-both-sort-directions.md` (belum diposting)

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-SU-E2E-194` | AdminConsole / SettingsUser | User List Sort: Sort 3-State Kelas Teks dengan Nilai Kosong di Akhir dan di Awal | High / Positive | Dalam | Lolos tak lengkap |

### BT-GS-IMP-40: GET /v2/import/global_settings/lookups/edit-options answers the Division and Position option sets as items: [""] with total 6 (one empty string for s… (1 spek)

**Verifikasi:** Draf ada, menunggu "go" owner. Draf `iam-import-options-divisions-positions-return-one-blank-item.md`, belum diposting.

Draf: `iam-import-options-divisions-positions-return-one-blank-item.md` (belum diposting)

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-IMPORT-E2E-103` | GlobalSettings / Import | Edit Mode Client C: FK Division dan Position pada draft User, AI Accept dan Dismiss pada sel, tombo… | High / Positive | Dalam | Lolos tak lengkap |

### BT-GS-IMP-41: PATCH /v2/iam/user-custom-fields/{id} (Overtime Hours, Decimal Places 2 -> 1, as Client E's second admin) answers 409 {"code":"decimal_places_locked"… (1 spek)

**Verifikasi:** Perlu draf issue. Belum ada issue dan draf (iam `user-custom-fields`, 409 `decimal_places_locked`).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-IMPORT-E2E-143` | GlobalSettings / Import | Late-binding Custom Field User saat commit: opsi Dropdown dihapus, Custom Field nonaktif, dan Decim… | Critical / Negative | Dalam | Lolos tak lengkap |

### BT-GS-IMP-42: The downloaded templates' header cells have a solid fill with no colour: xl/styles.xml holds <fills><fill><patternFill /></fill><fill><patternFill pa… (1 spek)

**Verifikasi:** Draf ada, menunggu "go" owner. Draf `import-template-header-white-text-on-no-fill.md`. Pembanding `import-service#22` (closed) hanya untuk kolom Custom Field, jadi bukan duplikat.

Draf: `import-template-header-white-text-on-no-fill.md` (belum diposting)

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-IMPORT-E2E-168` | GlobalSettings / Import | Isi dan styling berkas template: Custom Field Active di akhir, katalog saat diunduh, styling Sheet… | Critical / Positive | Dalam | Lolos tak lengkap |

### BT-GS-ROLE-15: PATCH/POST/DELETE /v2/iam/products/global_settings/roles/capabilities/users publish user.role_assigned only to the target user (user scope, userId =… (1 spek)

**Verifikasi:** Draf ada, menunggu "go" owner. Draf `iam-role-sse-role-assigned-target-only.md` ada di be-filing (tidak tertaut di laporan). Sebelum posting, cek `notification-service#13` (closed, push `user.role_assigned`).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-ROLE-E2E-107` | GlobalSettings / Role | Realtime: Auto-Revert Menghilangkan User dari Tab Total Control Sesi Admin Lain Tanpa Reload | High / Edge | Dalam | Lolos tak lengkap |

## Fitur BE belum ada (28 spek)


### BT-GAP-16: (tanpa baris temuan di laporan) (7 spek)

**Verifikasi:** Draf ada, menunggu "go" owner. Draf `ems-device-allocation-api-not-implemented.md` ditahan dengan alasan "out of sprint". Alasan itu sudah tidak cocok: sprint board 19 Nov baris 41 (Device Allocation) ada 🍰 tapi tanpa ⚙️. Posting menunggu owner.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-ACHA-E2E-023` | AdminConsole / DeviceAllocation | Submit Allocate Device: Double-Submit Hanya Memproses Satu Request dan Penolakan Server saat Saldo… | High / Edge | Dalam | Lolos tak lengkap |
| `TC-AC-ACHA-E2E-032` | AdminConsole / DeviceAllocation | Resubmit Diblokir Kondisi Data: Validasi Quantity, Saldo Kurang, Client Tidak Valid, dan Kantong Su… | High / Edge | Dalam | Lolos tak lengkap |
| `TC-AC-ACHA-E2E-048` | AdminConsole / DeviceAllocation | Integritas Log: Satu Entri per Aksi, Entri Lama Immutable, dan Aksi Gagal Tidak Mengubah Allocation… | High / Edge | Dalam | Lolos tak lengkap |
| `TC-AC-ACHA-E2E-053` | AdminConsole / DeviceAllocation | Konfigurasi dan Data Master: Dibaca Live atau Snapshot (Harga, Nama Client, Pengirim, Paid From, Al… | High / Edge | Dalam | Lolos tak lengkap |
| `TC-AC-ACHA-E2E-056` | AdminConsole / DeviceAllocation | Multi-Konteks: Konflik Dua Approver, Review Basi Setelah Cancel atau Edit, Edit Bersamaan Dua Sesi,… | High / Edge | Dalam | Lolos tak lengkap |
| `TC-AC-ACHA-E2E-057` | AdminConsole / DeviceAllocation | Race Commit Timeout Auto-Cancel Melawan Cancel Manual dan Approve | High / Edge | Dalam | Lolos tak lengkap |
| `TC-AC-ACHA-E2E-061` | AdminConsole / DeviceAllocation | Plan Gating: Modul Device Allocation Berperilaku Sama pada Plan Terendah dan Plan Tertinggi | Medium / Positive | Dalam | Lolos tak lengkap |

### BT-114: No way to create an Import User Login draft from a test: the Import page's CSV upload, the draft save and Create Missing Options have no test route a… (6 spek)

**Verifikasi:** Basi atau sudah selesai. Basi: baris BT sendiri sudah dikoreksi 7 Nov (backend Import ada, `/v2/import/global_settings`), dan skrip gs sudah membuat draf lewat `importDraftJob`. Sesi gs mengganti tag dengan penyebab dari run terbaru (mis. DIV-072: 403 `plan_required`).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-UCF-E2E-074` | GlobalSettings / CustomFieldUser | Import User Login: Kolom Custom Field di Staging Table, Kolom Tak Dikenal, Create Missing Options (… | High / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-DIV-E2E-071` | GlobalSettings / Division | Import Create Missing Divisions: Edit, Delete In-Use, dan Pencatatan Create | Medium / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-DIV-E2E-072` | GlobalSettings / Division | Import Create Missing Divisions: Master Data Count Limit dan Duplicate Race | High / Negative | Dalam | Gagal |
| `TC-GS-NLU-E2E-112` | GlobalSettings / NonLoginUser | Absence log: Edit tanpa perubahan, Import, dan Delete Login User pointer | High / Edge | Dalam | Lolos tak lengkap |
| `TC-GS-NLU-E2E-116` | GlobalSettings / NonLoginUser | Sinkronisasi Import dan Convert: Detail Login User, Changelog, tab Non-Login User | Medium / Edge | Dalam | Lolos tak lengkap |
| `TC-GS-POS-E2E-044` | GlobalSettings / Position | Pencatatan Create, Edit, Delete, Bulk Delete Campuran, Snapshot Rename, Kapitalisasi, Create Missin… | Critical / Positive | Dalam | Lolos tak lengkap |

### BT-GAP-37: (tanpa baris temuan di laporan) (4 spek)

**Verifikasi:** Basi atau sudah selesai. Basi: API License Allocation sudah ada (`enterprise-management-service#317` dan `#318` terbuka untuk route `/license-allocations`). Draf `ems-license-allocation-license-api-not-implemented.md` dipindah ke archive. Sesi ac retag LA 010/040/053/073 dari run terbaru.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-LA-E2E-010` | AdminConsole / LicenseAllocationLicense | Modal Allocation Log: Loading dan Immutability Entri | Medium / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-LA-E2E-040` | AdminConsole / LicenseAllocationLicense | Cost Terkunci: Pembulatan Half-up, Cost Nol, dan Nominal Sama dari Preview sampai Capture | High / Edge | Dalam | Lolos tak lengkap |
| `TC-AC-LA-E2E-053` | AdminConsole / LicenseAllocationLicense | Preview Cost Hari Terakhir Term dan Zona Waktu Plan Owner | High / Edge | Dalam | Lolos tak lengkap |
| `TC-AC-LA-E2E-073` | AdminConsole / LicenseAllocationLicense | Job Timeout Auto-Cancel vs Approve pada Batas SLA | High / Edge | Dalam | Lolos tak lengkap |

### BT-22: Admin Console > Settings > User is not sliced, so its Resend Activation Email row action does not exist in the app; (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: pemilik di baris BT = fe (row action Resend Activation Email di Admin Console > Settings > User). Diurus Integration A.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-ACT-E2E-025` | Auth / AccountActivation | Activation Email dari Admin Console dan Resend | Critical / Positive | Dalam | Lolos tak lengkap |

### BT-AC-ACC-32: contract drift, skipped, no issue: Activate Trial on an Archived Client answers 403 client_suspended_or_expired (LLD trials step 3) while the PRD (AC… (1 spek)

**Verifikasi:** Perlu draf issue. Contract drift (PRD vs LLD trials). Sesuai aturan, issue untuk pemilik LLD (enterprise-management), spek tetap di-skip dengan gap tag. Tulisan "no issue" di baris BT bertentangan dengan aturan itu.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-ACC-E2E-312` | AdminConsole / Client | Auto-Reactivate Client Archived: Add Subscription Mode New, Permintaan Di-Reject atau Di-Approve, d… | High / Positive | Dalam | Lolos tak lengkap |

### BT-AC-DS-17: Contract drift (PRD/spec vs openapi), not a code bug: a mixed DELETE /v2/enterprise-management/device-skus (one id already removed by another actor,… (1 spek)

**Verifikasi:** Perlu draf issue. Contract drift (PRD/spec vs openapi `DELETE device-skus`). Issue untuk pemilik LLD (enterprise-management).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-DS-E2E-086` | AdminConsole / SettingsDeviceSku | Bulk Delete: Seluruh SKU Terpilih Dihapus Pelaku Lain dan Satu Terhapus Sisanya Berstok | Critical / Edge | Dalam | Lolos tak lengkap |

### BT-GS-GSET-5: CONTRACT-DRIFT (see decisions.md): PUT /v2/enterprise-management/general-settings with sessionIdleTimeout: "Never" (a string) answers 422 … "Expected… (1 spek)

**Verifikasi:** Basi atau sudah selesai. BT ditutup 19 Nov lewat D-270 (bukan bug BE). GSET-050 sekarang lolos.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-GSET-E2E-050` | GlobalSettings / GeneralSettings | PUT 422 B | High / Negative | Dalam | Lolos tak lengkap |

### Tema: 108, 109 : the Group-Mix Principal (#8) cannot be seeded (fixture notSeedable.groupMix) (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: Principal hanya satu per backend (`ensurePrincipalTenant`), spec tanpa tag `principal` tidak memakainya. Butuh keputusan Coordinator (tag atau spec defect), bukan issue.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-PF-E2E-040` | AdminConsole / PlansLicensingPlansFeatures | Masking Assigned Clients - Total Control, Read Only Account-Wide, Dialog Cannot Archive Plan, Downl… | High / Positive | Dalam | Lolos tak lengkap |

### Tema: Data FAMS/SAMS (aset Fixed Asset, Supply Asset) tidak bisa dibuat dari tes (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: data Supply Asset di luar semua sprint; NLU-116 sudah sprint-gap (SG-USER-1, SG-USER-7).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-NLU-E2E-116` | GlobalSettings / NonLoginUser | Sinkronisasi Import dan Convert: Detail Login User, Changelog, tab Non-Login User | Medium / Edge | Dalam | Lolos tak lengkap |

### Tema: a new Active subscription for PT Baru Aktif made in Allocation > Client Subscription (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Belum ada baris BT; sesi ac menulis kebutuhannya (subscription Active baru dari Allocation) dulu.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-PF-E2E-175` | AdminConsole / PlansLicensingPlansFeatures | Tab Assigned Clients: empty state, subscription baru dari Allocation, dan navigasi ke Client Detail | High / Positive | Dalam | Lolos tak lengkap |

### Tema: the Group-Mix Principal (#8) cannot be seeded (fixture notSeedable.groupMix) (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: Principal hanya satu per backend (`ensurePrincipalTenant`), spec tanpa tag `principal` tidak memakainya. Butuh keputusan Coordinator (tag atau spec defect), bukan issue.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-PF-E2E-039` | AdminConsole / PlansLicensingPlansFeatures | Masking Assigned Clients per Baris Group Role - Zero Access, Read Only, CRUD, dan Hak Parsial | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: the Wallet price catalog is unreachable in remote mode (no contract operation) (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: Pricing di luar semua sprint (sprint board, owner 10 Nov) → `sprint-gap`.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-PF-E2E-056` | AdminConsole / PlansLicensingPlansFeatures | Estimated Reference Price pada Edit Custom Plan serta Create dan Edit Default Plan | High / Positive | Dalam | Lolos tak lengkap |

### Tema: the asynchronous export above 5.000 rows (1 spek)

**Verifikasi:** Luar filter. Semua spek di entri ini di luar filter, jadi tidak dibuatkan issue (aturan Filter).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-PP-E2E-047` | AdminConsole / SettingsPrivacyPolicy | Download CSV Lebih dari 5.000 Baris Diproses Sinkron (Riwayat D) | Medium / Edge | Luar | Lolos tak lengkap |

### Tema: the baseline count of the Account deleted rows for Wulan Kusuma — no action reads Activity Log rows of a deleted Client (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan baca Activity Log Client yang dihapus; belum ada baris BT. Sesi ac.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-024` | Auth / SessionManagement | App Access Revoke dan Delete Client: Pemutusan Sesi-Produk | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: the group-mix actor (a Group Role manage_active_client per Group) cannot be seeded: iam assigns a Group Role per Group and the suite creates no Group… (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: Principal hanya satu per backend (`ensurePrincipalTenant`), spec tanpa tag `principal` tidak memakainya. Butuh keputusan Coordinator (tag atau spec defect), bukan issue.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-PF-E2E-127` | AdminConsole / PlansLicensingPlansFeatures | Lintas Modul: Cap Custom Field FAMS dan Perubahan Role dan Permission Berlaku pada Pemuatan Berikut… | High / Positive | Dalam | Lolos tak lengkap |

## Helper atau seed dari BE (189 spek)


### BT-AC-HS-1: (tanpa baris temuan di laporan) (42 spek)

**Verifikasi:** Draf ada, menunggu "go" owner. Draf PR helper `pr-helper-ems-dev-hardware-stock-seed-and-age.md` (E5).

Draf: `pr-helper-ems-dev-hardware-stock-seed-and-age.md` (belum diposting)

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-ACHS-E2E-001` | AdminConsole / HardwareStock | Screening Stock List: Toolbar, Overlay Row Action, dan Tanpa Kolom Allocated atau Checkbox | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-003` | AdminConsole / HardwareStock | Empty State Genuinely Kosong dan No Results Stock Detail | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-007` | AdminConsole / HardwareStock | Screening Stock Detail Tab Available untuk Semua Tipe SKU | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-020` | AdminConsole / HardwareStock | Role Matrix: Visibilitas Elemen Stock List, Stock Detail, dan Approvals per Role | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-021` | AdminConsole / HardwareStock | Role Matrix Negatif: Menu Sidebar Hidden dan Direct URL Ditolak | High / Negative | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-022` | AdminConsole / HardwareStock | Scope Stock List, Stock Detail, dan Download per Aktor Distributor dan Principal | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-084` | AdminConsole / HardwareStock | Dialog Detail History, Badge Approval, dan Visibilitas Subject | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-092` | AdminConsole / HardwareStock | Hardware Log: Screening, Urutan, Read-Only, dan Scope | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-104` | AdminConsole / HardwareStock | Resilience Baca: Error Load dan Try Again | High / Negative | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-120` | AdminConsole / HardwareStock | Search Stock List: Siklus Kotak, Kolom Teks, Badge, dan Angka, Empty State, Kolom Non-Searchable, V… | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-121` | AdminConsole / HardwareStock | Filter Stock List: Screening Panel, Isi Opsi, Apply per Field, Opsi Tanpa Nilai Kosong, dan State L… | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-123` | AdminConsole / HardwareStock | Sort Stock List: Siklus 3-State Semua Kolom, Urutan Default, Nilai Kosong, Tie-Break, Kolom Non-Sor… | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-130` | AdminConsole / HardwareStock | Search Stock Detail Tab Available: Siklus Kotak, Kolom Teks, Badge, Pengguna, dan Angka, Empty Stat… | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-131` | AdminConsole / HardwareStock | Filter Stock Detail Tab Available: Screening Panel, Isi Opsi, dan Apply per Field | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-134` | AdminConsole / HardwareStock | Column Visibility dan Setup Column Stock Detail Tab Available: Screening Overlay dan Popup, Kelas D… | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-137` | AdminConsole / HardwareStock | Download Stock Detail Tab Available: Nama Berkas, Cakupan Search dan Seluruh Halaman, Kolom Hidden,… | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-160` | AdminConsole / HardwareStock | Search Stock Detail Tab In Use | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-161` | AdminConsole / HardwareStock | Filter Tab In Use Screening Opsi dan Apply per Field | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-162` | AdminConsole / HardwareStock | Filter Tab In Use Kombinasi Chip AND OR dan Indikator | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-163` | AdminConsole / HardwareStock | Sort Tab In Use | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-164` | AdminConsole / HardwareStock | Column Visibility dan Setup Column Tab In Use Kelas Data dan Power | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-167` | AdminConsole / HardwareStock | Download Tab In Use Nama Berkas Cakupan dan Kolom Hidden | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-200` | AdminConsole / HardwareStock | Search Approvals > Hardware Stock Tab History | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-201` | AdminConsole / HardwareStock | Filter Approvals > Hardware Stock Tab History: Screening, Opsi, dan Apply per Field | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-202` | AdminConsole / HardwareStock | Filter Approvals > Hardware Stock Tab History: Kombinasi Chip, AND/OR, dan Indikator | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-203` | AdminConsole / HardwareStock | Sort Approvals > Hardware Stock Tab History | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-206` | AdminConsole / HardwareStock | Pagination dan Kombinasi Empat Kontrol Approvals > Hardware Stock Tab History | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-207` | AdminConsole / HardwareStock | Download Approvals > Hardware Stock Tab History: Nama Berkas, Cakupan, dan Kolom Hidden | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-222` | AdminConsole / HardwareStock | Filter Popup Event Log: Kombinasi Chip, AND/OR, dan Indikator | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-223` | AdminConsole / HardwareStock | Sort Popup Event Log | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-227` | AdminConsole / HardwareStock | Download Popup Event Log: Nama Berkas, Cakupan, dan Kolom Hidden | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-240` | AdminConsole / HardwareStock | Isi Sel Stock List: Badge, Hitungan, Link SKU, dan Placeholder Foto | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-241` | AdminConsole / HardwareStock | Screening Stock Detail Tab In Use: Layout, Badge Status, Row Action Read-Only, dan Status Null | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-242` | AdminConsole / HardwareStock | Format Tanggal dan Waktu General Settings di Semua Surface Hardware Stock | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-244` | AdminConsole / HardwareStock | Tidak Ada Plan Gating: Add Stock Identik pada Tiap Tier Plan | Medium / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-245` | AdminConsole / HardwareStock | State Tenant Suspended dan Expired: Write Lockdown Add Stock, Sync, Delete, dan Approvals | High / Negative | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-247` | AdminConsole / HardwareStock | Validasi Serial Number Add Stock Manual Diblokir | High / Negative | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-264` | AdminConsole / HardwareStock | Dialog dan Sukses Delete Unit | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-269` | AdminConsole / HardwareStock | Approve dan Reject Activation Collision, State Submitting, dan Klik Ganda | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-271` | AdminConsole / HardwareStock | Multi-Konteks: Race Keputusan Approval | High / Negative | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-272` | AdminConsole / HardwareStock | Multi-Konteks: Race Add Stock dan Delete | High / Edge | Dalam | Lolos tak lengkap |
| `TC-AC-ACHS-E2E-287` | AdminConsole / HardwareStock | Filter Stock Detail Tab Available: Kombinasi Chip, OR dan AND, Search, Draft, Indikator, Kolom Ters… | High / Positive | Dalam | Lolos tak lengkap |

### BT-GS-IMP-1: Draft age (BE helper ask BT-GAP-H8i): no test-only route moves an import draft's created_at back for a test tenant. (29 spek)

**Verifikasi:** Draf ada, menunggu "go" owner. Draf PR helper `pr-helper-import-draft-age.md` (E5). Kode ada di `test/import-dev-age`, image belum dibangun.

Draf: `pr-helper-import-draft-age.md` (belum diposting)

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-IMPORT-E2E-001` | GlobalSettings / Import | Screening Halaman Import dengan Draft Brand, Sub-Tab Default, Skeleton Loading, dan Unsaved Banner… | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-004` | GlobalSettings / Import | Unsaved Banner pada Client C: Tampil Bersama Draft Division, Tanggal Tetap Setelah Edit dan Append,… | High / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-010` | GlobalSettings / Import | Role Positif: Default User dan Import data (Create) Menjalankan Upload, Confirm Mapping, Import, Sa… | High / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-044` | GlobalSettings / Import | Defense-in-depth: Permintaan Langsung Ditolak 403 untuk Import data (Read Only), Read Only, dan Tan… | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-061` | GlobalSettings / Import | Client Expired: Discard Draft Ditolak 403 dengan Toast Khusus; Permintaan Langsung dan Create Missi… | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-063` | GlobalSettings / Import | Role Matrix: Visibilitas dan State Elemen Halaman Import untuk Total Control, Default User, dan Imp… | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-064` | GlobalSettings / Import | Role Matrix: Elemen Disabled dan Hidden untuk Read Only dan Import data (Read Only) pada Halaman Im… | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-068` | GlobalSettings / Import | Konflik Kunci Sesi Edit: Pintu Masuk Admin Kedua Ditolak 409 dengan Dialog Draft Is Being Edited, B… | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-069` | GlobalSettings / Import | Aksi Admin Kedua Ditolak 409 saat Kunci Dipegang: Append, Confirm Mapping, Remove, Bulk Delete, Dis… | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-075` | GlobalSettings / Import | Kunci Kedaluwarsa: Save Pemegang Lama Diproses Normal bila Belum Diambil, Ditolak 409 bila Sudah Di… | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-080` | GlobalSettings / Import | Aksi Staging Table Sebelum Commit Tidak Dicatat di Changelog Import, System Log, dan Activity Log | High / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-091` | GlobalSettings / Import | Edit Mode: Error Callout dan chip Disabled, Upload File dan Discard Disabled dengan Download Templa… | High / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-112` | GlobalSettings / Import | Delete All Rows dari Error Summary Callout dan penekanan saran AI dihapus oleh Remove dan Discard D… | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-114` | GlobalSettings / Import | Dialog konfirmasi (backdrop, Esc) dan Discard Draft: screening, Cancel, double-submit tombol konfir… | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-124` | GlobalSettings / Import | Create Missing Divisions dan Positions bulk dari Callout: dedup nama tidak peka huruf besar-kecil;… | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-135` | GlobalSettings / Import | Partial Commit: baris error tetap, duplicate dihapus, error diperbaiki lalu commit ulang, dan penom… | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-136` | GlobalSettings / Import | Banner Hasil Commit: dapat ditutup, tampil tanpa Unsaved Banner, dan batas usia 23 jam 59 menit dan… | High / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-145` | GlobalSettings / Import | Defense-in-depth: request langsung ke server saat committing atau tanpa draft ditolak (conflict ata… | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-147` | GlobalSettings / Import | Fault injection: Accept/Dismiss saran gagal atau tanpa respons, gagal memulai commit, timeout Impor… | High / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-150` | GlobalSettings / Import | Multi-konteks Client E: commit bersamaan dua sesi, Banner Hasil Commit sekali per administrator, ha… | Critical / Edge | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-152` | GlobalSettings / Import | Kontrol worker commit: tombol global Disabled dengan tooltip selama committing, fitur baca tetap be… | Critical / Edge | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-156` | GlobalSettings / Import | Kontrol worker commit: Import, Discard, Upload, Save kunci kedaluwarsa, Confirm Mapping dari halama… | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-158` | GlobalSettings / Import | Kontrol worker commit: pelanjutan otomatis setelah batas tanpa kemajuan tanpa memproses ulang baris… | Critical / Edge | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-159` | GlobalSettings / Import | Kontrol worker commit: commit berhenti tanpa Banner Hasil Commit, notifikasi stopped, duplicate tet… | High / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-160` | GlobalSettings / Import | Notifikasi progres commit: awal, pembaruan in-place per batch, selesai dengan Detail, selesai denga… | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-177` | GlobalSettings / Import | Harness eksternal worker commit: dijeda atau dihentikan (entri rows remaining, tanpa entri bila 0 t… | Critical / Edge | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-181` | GlobalSettings / Import | Absence log: edit sel, duplikasi, hapus baris, Discard Draft tidak mencatat Changelog Import, Syste… | High / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-184` | GlobalSettings / Import | Absence log: aktivitas pre-commit (edit, remove, discard) tidak menambah entri Changelog Import (se… | High / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-216` | GlobalSettings / Import | Draft dibagikan ke seluruh admin berkapabilitas dalam organisasi yang sama (Import data Create dan… | High / Positive | Dalam | Lolos tak lengkap |

### BT-GS-MYPROFILE-4: Change Password counter and lock of a test user: set the counter (2, 3), set a 15-minute lock with a retry-at instant (09:15; (14 spek)

**Verifikasi:** Bukan BE. Baris BT sendiri: sudah direklasifikasi jadi sprint-gap (D-098). My Profile (sprint board baris 51) tanpa 🍰.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-PROFILE-E2E-019` | GlobalSettings / MyProfile | Change Password: Current Password salah, hitungan percobaan, dan urutan evaluasi | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-PROFILE-E2E-021` | GlobalSettings / MyProfile | Change Password: batas 72 karakter, multi-aturan, non-ASCII, sama dengan password aktif, dan anti-r… | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-PROFILE-E2E-022` | GlobalSettings / MyProfile | Change Password berhasil: toast, saving state, klik ganda, auto-hide 4 detik, tanpa guard | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-PROFILE-E2E-023` | GlobalSettings / MyProfile | Change Password berhasil: login password baru, reset counter Change Password dan Login | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-PROFILE-E2E-024` | GlobalSettings / MyProfile | Change Password: hitungan independen dari Login dan reset oleh Reset Password | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-PROFILE-E2E-028` | GlobalSettings / MyProfile | Change Password: Lock 15 Menit (Toast, Format 12 Jam, Timezone, Note User Log, Time Format Berubah) | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-PROFILE-E2E-029` | GlobalSettings / MyProfile | Change Password: [Save] Disabled saat Modal Dibuka Terkunci, Tooltip, Loading Baca Lock, dan Fail-O… | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-PROFILE-E2E-030` | GlobalSettings / MyProfile | Change Password: Batas Waktu Boleh-Coba-Lagi (Satu Langkah Sebelum, Tepat, dan Setelah) | High / Edge | Dalam | Lolos tak lengkap |
| `TC-GS-PROFILE-E2E-031` | GlobalSettings / MyProfile | Change Password: Lock 1 Jam, Tier Wajib-Reset, dan Tidak Lepas oleh Waktu | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-PROFILE-E2E-032` | GlobalSettings / MyProfile | Change Password: Reset Hitungan Harian per Timezone, Lock Melewati Tengah Malam, dan Eskalasi 7 Hari | High / Edge | Dalam | Lolos tak lengkap |
| `TC-GS-PROFILE-E2E-051` | GlobalSettings / MyProfile | Pencatatan Change Password: Note Locked 15 Menit, 1 Jam, Wajib Reset, dan Eskalasi 7 Hari | High / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-PROFILE-E2E-061` | GlobalSettings / MyProfile | Multi-Sesi: Change Password Mengakhiri Sesi Lain, Dialog Password Changed, dan Lock Lintas Sesi | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-PROFILE-E2E-062` | GlobalSettings / MyProfile | Multi-Sesi: Sesi yang Kalah, Dua Request Bersamaan, dan User Log Logout | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-PROFILE-E2E-067` | GlobalSettings / MyProfile | Defense-in-Depth: Payload Edit Photo Tidak Sah (422) dan Request Change Password Langsung (Field-Le… | Critical / Negative | Dalam | Lolos tak lengkap |

### BT-GS-IMP-3: Commit worker control (BE helper ask BT-GAP-H10i): no test-only route pauses, resumes or stops a job's commit worker or sets its batch progress. (12 spek)

**Verifikasi:** Perlu draf issue. Belum ada issue dan draf (helper import-service untuk kontrol worker commit).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-IMPORT-E2E-145` | GlobalSettings / Import | Defense-in-depth: request langsung ke server saat committing atau tanpa draft ditolak (conflict ata… | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-150` | GlobalSettings / Import | Multi-konteks Client E: commit bersamaan dua sesi, Banner Hasil Commit sekali per administrator, ha… | Critical / Edge | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-152` | GlobalSettings / Import | Kontrol worker commit: tombol global Disabled dengan tooltip selama committing, fitur baca tetap be… | Critical / Edge | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-153` | GlobalSettings / Import | Kontrol worker commit: Accept AI dan Create Missing (Divisions, Positions) Disabled dengan tooltip… | High / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-154` | GlobalSettings / Import | Kontrol worker commit: keanggotaan batch aktif menentukan Remove dan checkbox Disabled atau Enabled | Critical / Edge | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-155` | GlobalSettings / Import | Kontrol worker commit: Remove, Bulk Delete, dan Delete All Rows dari halaman basi (partial di luar… | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-156` | GlobalSettings / Import | Kontrol worker commit: Import, Discard, Upload, Save kunci kedaluwarsa, Confirm Mapping dari halama… | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-157` | GlobalSettings / Import | Kontrol worker commit: Accept AI dan Create Missing dari halaman basi saat committing memunculkan d… | High / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-158` | GlobalSettings / Import | Kontrol worker commit: pelanjutan otomatis setelah batas tanpa kemajuan tanpa memproses ulang baris… | Critical / Edge | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-159` | GlobalSettings / Import | Kontrol worker commit: commit berhenti tanpa Banner Hasil Commit, notifikasi stopped, duplicate tet… | High / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-160` | GlobalSettings / Import | Notifikasi progres commit: awal, pembaruan in-place per batch, selesai dengan Detail, selesai denga… | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-177` | GlobalSettings / Import | Harness eksternal worker commit: dijeda atau dihentikan (entri rows remaining, tanpa entri bila 0 t… | Critical / Edge | Dalam | Lolos tak lengkap |

### Tema: Browser License, Concurrent User dan seat produk tidak bisa diatur atau dibaca dari tes (8 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan seed seat/Browser License; belum ada baris BT (023 dan 026 di luar filter). Sesi ac.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-023` | Auth / SessionManagement | Sesi Yatim Bekas App-Kill: ID Device dan Batas Heartbeat 60 Detik | High / Edge | Luar | Gagal |
| `TC-AUTH-SES-E2E-024` | Auth / SessionManagement | App Access Revoke dan Delete Client: Pemutusan Sesi-Produk | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-AUTH-SES-E2E-025` | Auth / SessionManagement | Client Suspended: Dialog Access Restricted, OK, dan Unsuspend | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-AUTH-SES-E2E-026` | Auth / SessionManagement | Client Suspended: Push Terlewat, Tampil Ulang, Write Guard, dan Bulk Suspend | High / Edge | Luar | Lolos tak lengkap |
| `TC-AUTH-SES-E2E-027` | Auth / SessionManagement | User Dinonaktifkan di Produk Fixed Asset: Pemutusan Sesi-Produk | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AUTH-SES-E2E-029` | Auth / SessionManagement | Invalidasi Semua Sesi Web, Mobile, dan Sesi-produk saat Akun Dinonaktifkan atau Dihapus | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AUTH-SES-E2E-034` | Auth / SessionManagement | Sesi-produk Bersama Web dan Mobile | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AUTH-SES-E2E-055` | Auth / SessionManagement | Change Password dan Reset Password Meng-invalidate Sesi Aktif Lintas Web dan Mobile | Critical / Positive | Dalam | Lolos tak lengkap |

### BT-AC-CS-13: The dev seed PUT /dev/clients/{code}/subscriptions writes none of authorized_at, requested_by_id and the subscription_price_snapshots lines of the te… (6 spek)

**Verifikasi:** Perlu draf issue. Belum ada draf sendiri (dev seed subscriptions di enterprise-management). CS-010 dan CS-033 sudah sprint-gap SG-AC-PRICE-1. Yang tersisa: CS-005, 058, 101, 152.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-CS-E2E-005` | AdminConsole / LicenseAllocationSubscription | List: Baris Riwayat, Sel Plan, dan Sel Plan Owner | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-CS-E2E-010` | AdminConsole / LicenseAllocationSubscription | Detail: Subscription Info | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-CS-E2E-033` | AdminConsole / LicenseAllocationSubscription | Form Renew: Validasi dan Preview Renewal | High / Negative | Dalam | Lolos tak lengkap |
| `TC-AC-CS-E2E-058` | AdminConsole / LicenseAllocationSubscription | Edit: Validasi Duration, Start Date, dan Ceiling Trial | High / Negative | Dalam | Lolos tak lengkap |
| `TC-AC-CS-E2E-101` | AdminConsole / LicenseAllocationSubscription | List Download: Isi Berkas CSV dan XLSX | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-CS-E2E-152` | AdminConsole / LicenseAllocationSubscription | Job: Timeout Auto-Cancel Term Convert dan Edit | High / Positive | Dalam | Lolos tak lengkap |

### BT-GS-IMP-2: Edit-lock TTL aging (BE helper ask BT-GAP-H9i): no test-only route moves the edit session lock's last mutation back. (5 spek)

**Verifikasi:** Perlu draf issue. Belum ada issue dan draf (helper import-service, aging TTL edit-lock).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-IMPORT-E2E-055` | GlobalSettings / Import | Kunci Sesi Edit: Izin Create Dicabut saat Sesi Edit Aktif, Save Ditolak 403, Dialog Draft Is Being… | High / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-074` | GlobalSettings / Import | TTL Kunci Sesi Edit 10 Menit: Kedaluwarsa Tepat 10 Menit, Masih Berlaku pada Menit ke-9, dan Hitung… | Critical / Edge | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-075` | GlobalSettings / Import | Kunci Kedaluwarsa: Save Pemegang Lama Diproses Normal bila Belum Diambil, Ditolak 409 bila Sudah Di… | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-094` | GlobalSettings / Import | Save diblokir all-or-nothing: wajib, panjang live (karakter ke-121), urutan pesan, tiap Import Type… | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-156` | GlobalSettings / Import | Kontrol worker commit: Import, Discard, Upload, Save kunci kedaluwarsa, Confirm Mapping dari halama… | Critical / Negative | Dalam | Lolos tak lengkap |

### BT-GS-MYPROFILE-5: Time Format (12 h / 24 h) and timezone of a user (Pre-setup #7: 24 h, Asia/Jakarta; (4 spek)

**Verifikasi:** Bukan BE. Bukan BE: My Profile (sprint board baris 51) tanpa 🍰, jadi sprint-gap (D-098).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-PROFILE-E2E-019` | GlobalSettings / MyProfile | Change Password: Current Password salah, hitungan percobaan, dan urutan evaluasi | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-PROFILE-E2E-028` | GlobalSettings / MyProfile | Change Password: Lock 15 Menit (Toast, Format 12 Jam, Timezone, Note User Log, Time Format Berubah) | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-PROFILE-E2E-030` | GlobalSettings / MyProfile | Change Password: Batas Waktu Boleh-Coba-Lagi (Satu Langkah Sebelum, Tepat, dan Setelah) | High / Edge | Dalam | Lolos tak lengkap |
| `TC-GS-PROFILE-E2E-032` | GlobalSettings / MyProfile | Change Password: Reset Hitungan Harian per Timezone, Lock Melewati Tengah Malam, dan Eskalasi 7 Hari | High / Edge | Dalam | Lolos tak lengkap |

### Tema: TAG Stock belum punya backend di stack ini (4 spek)

**Verifikasi:** Issue/helper sudah ada. Basi: API TAG Stock sudah ada (`hardware-tagging-service#79` closed); route seed `hardware-tagging-service#128` (WIP). Sesi ac retag dari run terbaru.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-DS-E2E-078` | AdminConsole / SettingsDeviceSku | Delete SKU Single Berhasil: Klik Ganda Satu Penghapusan dan Riwayat Transaksi Tetap Terbaca | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-DS-E2E-154` | AdminConsole / SettingsDeviceSku | Sinkron Modul Stok: Register SKU Hardware dan TAG Menjadi Pilihan Add Stock dan Baris Stock List | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-DS-E2E-156` | AdminConsole / SettingsDeviceSku | Sinkron Modul Stok: Delete dan Bulk Delete Menghilangkan Pilihan Stok serta Add Stock Mengaktifkan… | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-DS-E2E-194` | AdminConsole / SettingsDeviceSku | Sinkron Modul Stok: Edit Kode SKU, Range Type, dan User TAG Tercermin pada Stock List Hardware Stoc… | High / Positive | Dalam | Lolos tak lengkap |

### BT-13: The Privacy Policy is one document for the whole platform. (3 spek)

**Verifikasi:** Bukan BE. Diputuskan owner 29 Okt: aturan jadwal run (suite jalan sendiri, baseline dipulihkan di `after`). Bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-OTP-E2E-030` | Auth / LoginOtp | Ketahanan Verify OTP dan Konfirmasi Agreement terhadap Error Server dan Timeout | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-AUTH-LP-E2E-028` | Auth / LoginPassword | Ketahanan Login terhadap Kegagalan Penyedia: reCAPTCHA, Geo-IP, dan Versi Privacy Policy | High / Negative | Dalam | Lolos tak lengkap |
| `TC-AUTH-LP-E2E-043` | Auth / LoginPassword | Tidak Ada Pencatatan Log pada Kondisi Lock, MFA Tertunda, Agreement Ditinggalkan, dan Policy Tak Te… | Critical / Negative | Dalam | Gagal |

### BT-AC-ACC-28: POST /dev/time/age (EMS) has no clients scope: a Client's Last Updated cannot be backdated (285, 292) (3 spek)

**Verifikasi:** Perlu draf issue. Belum ada issue (`/dev/time/age` di enterprise-management belum punya scope `clients`). Bisa digabung ke draf `pr-helper-ems-time-age-groups-scope.md` (BT-AC-SG-6).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-ACC-E2E-003` | AdminConsole / Client | Isi Sel Kolom List Client: Company Name, Managed By, Modified By, dan Kolom Opsional | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACC-E2E-285` | AdminConsole / Client | Filter Client List: Last Updated Date Range Picker Satu Field, Rentang Inklusif, dan Tanggal Mulai… | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACC-E2E-292` | AdminConsole / Client | Sort Client List: Siklus Tiga State Ascending, Descending, dan Nonaktif pada Kolom Default dan Mana… | High / Positive | Dalam | Lolos tak lengkap |

### Tema: Device Allocation belum punya backend di stack ini (3 spek)

**Verifikasi:** Draf ada, menunggu "go" owner. Sama dengan BT-GAP-16: draf `ems-device-allocation-api-not-implemented.md` (held), menunggu owner.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-LCS-E2E-145` | AdminConsole / PlansLicensingLifecycleSettings | Approval Settings Konsumen: Timeout Auto-Cancel, Recalculation Batas, dan Warning H-24 pada Device… | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-LCS-E2E-146` | AdminConsole / PlansLicensingLifecycleSettings | Approval Settings Konsumen: Pengiriman Ulang Warning, Recalculation Berurutan, Reset, Progress Appr… | High / Edge | Dalam | Lolos tak lengkap |
| `TC-AC-LCS-E2E-147` | AdminConsole / PlansLicensingLifecycleSettings | Approval Settings Konsumen: Pembatalan Manual Bersamaan dengan Job Timeout | High / Edge | Dalam | Lolos tak lengkap |

### BT-114: Import: tidak ada route tes yang menjalankan job Import atau membuat draft-nya (lihat BT-114) (2 spek)

**Verifikasi:** Basi atau sudah selesai. Basi: baris BT sendiri sudah dikoreksi 7 Nov (backend Import ada, `/v2/import/global_settings`), dan skrip gs sudah membuat draf lewat `importDraftJob`. Sesi gs mengganti tag dengan penyebab dari run terbaru (mis. DIV-072: 403 `plan_required`).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-ACTLOG-E2E-038` | GlobalSettings / ActivityLog | Aksi Lain di User Action: Edit Permission System Role, Activate/Deactivate, Import | High / Positive | Dalam | Lolos tak lengkap |
| `TC-GS-IMPORT-E2E-180` | GlobalSettings / Import | Binary buffer: isi berkas Changelog CSV/XLSX (header, 30 baris, sheet, mengikuti Search dan kolom)… | High / Positive | Dalam | Lolos tak lengkap |

### BT-115: No test route or support action reads or sets a tenant's System Limits: the Master Data Count Limit and the Selection Limit. (2 spek)

**Verifikasi:** Luar filter. Semua spek di entri ini di luar filter, jadi tidak dibuatkan issue (aturan Filter).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-UCF-E2E-058` | GlobalSettings / CustomFieldUser | Download di Atas 5.000 Baris Tabel Custom Field: Loading Screen sampai Berkas Siap lalu Langsung Te… | Medium / Edge | Luar | Lolos tak lengkap |
| `TC-GS-NLU-E2E-075` | GlobalSettings / NonLoginUser | Download di Atas 5.000 Baris: Loading Screen lalu Berkas Terunduh | Medium / Edge | Luar | Lolos tak lengkap |

### BT-84: No route or action seeds the bulk volume that TC-GS-FILEMGR-E2E-054 needs: 5.001 active profile photos of one tenant, so the main table's CSV downloa… (2 spek)

**Verifikasi:** Luar filter. Semua spek di entri ini di luar filter, jadi tidak dibuatkan issue (aturan Filter).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-021` | GlobalSettings / FileManager | Bulk Delete dan Bulk Permanently Delete dengan 1.001 Baris Terseleksi | Medium / Edge | Luar | Lolos tak lengkap |
| `TC-GS-FILEMGR-E2E-054` | GlobalSettings / FileManager | Download Tabel Utama dengan 5.001 Baris | Medium / Edge | Luar | Lolos tak lengkap |

### BT-AC-ACC-38: (tanpa baris temuan di laporan) (2 spek)

**Verifikasi:** Ditahan / perlu baris BT atau bukti. Baris BT tidak ada di file temuan, jadi isi kebutuhannya tidak diketahui. Sesi ac menulis baris BT dulu.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-ACC-E2E-173` | AdminConsole / Client | Section Parent / Pengelola dan Section Default User pada Detail Client | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-ACC-E2E-177` | AdminConsole / Client | Default User di Detail Client Mengikuti Perubahan Global Settings Tanpa Muat Ulang | High / Positive | Dalam | Lolos tak lengkap |

### BT-AC-SG-6: A Settings Group's Created and Last Updated cannot be backdated: POST /v2/enterprise-management/dev/time/age has no groups scope (brands, measurement… (2 spek)

**Verifikasi:** Draf ada, menunggu "go" owner. Draf PR helper `pr-helper-ems-time-age-groups-scope.md` (belum diposting, belum live).

Draf: `pr-helper-ems-time-age-groups-scope.md` (belum diposting)

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-SG-E2E-053` | AdminConsole / SettingsGroup | Filter Tabel Utama: Modified By, Search Dropdown, dan Last Updated | High / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-SG-E2E-057` | AdminConsole / SettingsGroup | Sort Tabel Utama: Modified By, Last Updated, Pindah Kolom, dan Independen dari Search dan Filter | High / Positive | Dalam | Lolos tak lengkap |

### BT-FA-GRP-1: Aset terdaftar dalam group (Warehouse A: 24 Active + 2 Disposed; (2 spek)

**Verifikasi:** Bukan BE. Bukan BE: Group Detail > Tab Assets adalah sprint-gap (D-098). Baris BT juga baru berupa pertanyaan.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-FA-GRP-E2E-027` | FixedAsset / SettingsGroups | Tab Assets Detail Group: Himpunan Aset Exact-Match Belum Disposed/Deleted, Status Aturan Resolusi,… | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-FA-GRP-E2E-028` | FixedAsset / SettingsGroups | Klik Total Asset: Membuka Tab Assets, Total Asset 0 Empty State, dan Angka Realtime Setelah Aset Di… | Critical / Positive | Dalam | Lolos tak lengkap |

### BT-GS-MYPROFILE-7: A Storage quota that is not a whole GB (49.9 GB of Client #12) and a quota change as License Allocation makes it for a test tenant: PUT /dev/storage-… (2 spek)

**Verifikasi:** Bukan BE. Bukan BE: My Profile (sprint board baris 51) tanpa 🍰, jadi sprint-gap (D-098).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-PROFILE-E2E-059` | GlobalSettings / MyProfile | Storage Penuh atau Melebihi Kuota: Edit Photo Diblokir, Delete Photo Tetap Berhasil | Critical / Negative | Dalam | Lolos tak lengkap |
| `TC-GS-PROFILE-E2E-060` | GlobalSettings / MyProfile | Storage di Bawah Kuota, Tanpa Kuota, Cek Ledger, dan Perubahan Kuota di License Allocation | High / Edge | Dalam | Lolos tak lengkap |

### BT-GS-ROLE-6: A fresh test tenant's Default User comes back with isDefault: false and no row on any of the six system roles, so the Default User guards do not hold… (2 spek)

**Verifikasi:** Issue/helper sudah ada. Helper sudah dibangun: `pr-helper-ems-dev-create-default-user-id.md`, deploy di slot 2 pada 12 Nov. Slot 1 dan 3 menyusul di jendela Coordinator. Rerun LCS-018/027 di slot yang sudah memuatnya.

Draf: `pr-helper-ems-dev-create-default-user-id.md` (belum diposting)

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-LCS-E2E-018` | AdminConsole / PlansLicensingLifecycleSettings | Role Matrix Positif: Item Sidebar dan Halaman Lifecycle Settings Terbuka per Role | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-LCS-E2E-027` | AdminConsole / PlansLicensingLifecycleSettings | Role Matrix Positif: Default User Mengeksekusi Save dan Reset Tab Free Plan Settings | Critical / Positive | Dalam | Lolos tak lengkap |

### BT-LA-1: (tanpa baris temuan di laporan) (2 spek)

**Verifikasi:** Ditahan / perlu baris BT atau bukti. Baris BT tidak ada di file temuan. Sesi ac menulis baris BT dulu.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-LA-E2E-009` | AdminConsole / LicenseAllocationLicense | Screening Modal Allocation Log: Isi, Copy ID, Scroll, Empty State, dan Cara Tutup | Critical / Positive | Dalam | Lolos tak lengkap |
| `TC-AC-LA-E2E-114` | AdminConsole / LicenseAllocationLicense | Modal Changelog: Screening, Cakupan Seluruh Alokasi, Format Sel, Empty State, dan Tutup | Critical / Positive | Dalam | Lolos tak lengkap |

### BT-6: The dev reCAPTCHA placeholder (no site key) sends dev-placeholder, which iam rejects; (1 spek)

**Verifikasi:** Bukan BE. Diputuskan owner 29 Okt: pakai pasangan test key reCAPTCHA Google, pemilik fe. Bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-RST-E2E-043` | Auth / ResetPassword | Absence: Aksi Reset Password yang Tidak Boleh Dicatat pada Activity Log Session dan User Log | Critical / Negative | Dalam | Gagal |

### BT-AC-ACC-37: The dev Client status route (PATCH /dev/clients/{code}/status, Archived) overwrites Modified By with System, so an Archived Client whose last modifie… (1 spek)

**Verifikasi:** Perlu draf issue. Belum ada draf (route dev status Client menimpa Modified By dengan System). Bisa digabung ke draf `pr-helper-ems-dev-client-status-archived.md` (BT-AC-SG-5, route yang sama).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-ACC-E2E-003` | AdminConsole / Client | Isi Sel Kolom List Client: Company Name, Managed By, Modified By, dan Kolom Opsional | High / Positive | Dalam | Lolos tak lengkap |

### BT-AC-ACC-39: (tanpa baris temuan di laporan) (1 spek)

**Verifikasi:** Ditahan / perlu baris BT atau bukti. Baris BT tidak ada di file temuan. Sesi ac menulis baris BT dulu.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-ACC-E2E-313` | AdminConsole / Client | Job Lifecycle Otomatis dengan Jam Server Dimajukan: Auto-Archive Grace, Purge ke Deleted, Renewal P… | High / Positive | Dalam | Lolos tak lengkap |

### BT-AC-CS-28: A read of the per-product App Access of a Client's Default User (Not Yet Activated, made by POST /clients, no session of its own) as the Principal ad… (1 spek)

**Verifikasi:** Perlu draf issue. Baris BT ada, belum ada issue dan draf. Isi baris BT perlu dilengkapi sesi ac (request/response).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-CS-E2E-083` | AdminConsole / LicenseAllocationSubscription | Approvals: Trial Activation oleh Additional Approver Principal | Critical / Positive | Dalam | Lolos tak lengkap |

### BT-AC-CS-9: No bulk route for subscription terms: the dev plan route makes one paid term per test tenant, and a History row needs a write per row through the fea… (1 spek)

**Verifikasi:** Ditahan / perlu baris BT atau bukti. Ditahan Coordinator 10 Nov.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-CS-E2E-100` | AdminConsole / LicenseAllocationSubscription | List Download: Cakupan, Filter, Kolom, dan Volume 5.001 Baris | Critical / Positive | Dalam | Lolos tak lengkap |

### BT-AC-DN-1: BYO registered-unit fixture (no producer on stack): a Client's self-purchased (BYO) units of a Device Name are written by Jalur B activation (Global… (1 spek)

**Verifikasi:** Ditahan / perlu baris BT atau bukti. BE sudah mengumumkan route, tapi belum di-deploy. Bukan issue baru.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-DN-E2E-178` | AdminConsole / SettingsDeviceName | All TAGs: Pemilih Device Name Self-Purchased Template dan Registri Tag Jalur A/B setelah Rename | High / Positive | Dalam | Lolos tak lengkap |

### BT-AC-DS-2: No route creates Device SKUs in bulk. (1 spek)

**Verifikasi:** Luar filter. Semua spek di entri ini di luar filter, jadi tidak dibuatkan issue (aturan Filter).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-DS-E2E-175` | AdminConsole / SettingsDeviceSku | Volume Data: Download 5.001 Baris Memakai Loading Screen dan Tepat 5.000 Baris Tanpa Loading | High / Edge | Luar | Gagal |

### BT-AUTH-SES-1: draft ISSUE-DRAFT-iam-change-password-endpoint-missing.md (backend root) · draft (Gitea unreachable): iam does not implement the contract route PATCH… (1 spek)

**Verifikasi:** Issue/helper sudah ada. Issue sudah ada: `iam-service#238` (closed, kontrak dan route Change Password). Draf `ISSUE-DRAFT-iam-change-password-endpoint-missing.md` tidak diperlukan. Change Password ada di My Profile (baris 51, tanpa 🍰), jadi sprint-gap.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-ACAL-E2E-021` | AdminConsole / ActivityLog | Absence: Event Platform dan Download Tidak Tercatat | Critical / Negative | Dalam | Lolos tak lengkap |

### BT-GS-HHR-3: The HHR-1 bulk route makes Official stock units in the shared Principal stock, and deleteTestTenant neither frees nor removes them: a new tenant seed… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Sudah diperbaiki di helper (hardware-tagging hhr2a, slot 1 dan 2, 8 Nov). Rerun DS-189.

Draf: `ems-hhr3-in-use-units-block-delete.md` (belum diposting)

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-DS-E2E-189` | AdminConsole / SettingsDeviceSku | Bulk Delete: Hasil Aktual Menentukan Toast saat Preview Campuran Menjadi Homogen dan Homogen Menjad… | High / Edge | Dalam | Lolos tak lengkap |

### BT-GS-IMP-4: Large staging seed (BE helper ask BT-GAP-H11i): no test-only route writes a draft with 9,995 staging rows. (1 spek)

**Verifikasi:** Perlu draf issue. Belum ada issue dan draf (helper import-service, seed staging besar).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-IMPORT-E2E-142` | GlobalSettings / Import | Late-binding field User saat commit: Email, Employee ID, Access, dan Active Period menjadi tidak va… | High / Negative | Dalam | Lolos tak lengkap |

### BT-GS-TAG-12: No test route writes TAG Log entries (event, date, actor, previous status) for a TAG, so the TAG Log popup of a seeded TAG is always empty and no spe… (1 spek)

**Verifikasi:** Draf ada, menunggu "go" owner. Draf `pr-helper-tag-event-log-seed.md` / `pr-helper-tag-log-seed.md` (ditahan, belum diposting).

Draf: `pr-helper-tag-event-log-seed.md` (belum diposting)

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-TAG-E2E-062` | GlobalSettings / AllTags | Un-Retire Ditolak oleh Supply Asset saat Kuota Tipe Penuh atau Terpakai Melebihi Kuota | Medium / Edge | Dalam | Lolos tak lengkap |

### BT-GS-UOM-2: POST /dev/measurement-item-types (EMS 6237615) creates active item types only, and no route moves an item type to another unit: an inactive Asset Nam… (1 spek)

**Verifikasi:** Issue/helper sudah ada. Sebagian sudah ada: `enterprise-management-service#73` (merged, route dev untuk memindah item type). Sisa kebutuhan (`status`, `deleted`) ditambahkan ke issue itu sebagai komentar.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-UOM-E2E-058` | GlobalSettings / Measurement | Total Item di Header Unit Detail: Client, Principal, Nol, Relasi Nonaktif, Recycle Bin, dan Perubah… | Critical / Positive | Dalam | Lolos tak lengkap |

### BT-NEW-F2: BT-NEW-F2 — Pre-setup rows saved on 9, 10 and 11 Sep 2026: the suite seeds Custom Fields at run time (Last Updated = the run's day) and no route or a… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. ID belum terdaftar di file temuan (tidak ada baris BT). Kebutuhan: aging `updated_at` Custom Field User. Sesi gs mendaftarkan BT.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-UCF-E2E-052` | GlobalSettings / CustomFieldUser | Filter Panel Tabel Utama Custom Field: Screening, Logika OR dan AND, Chip, Opsi Dinamis, Draft, Cle… | Critical / Positive | Dalam | Lolos tak lengkap |

### BT-NEW-G2: BT-NEW-G2 — no route or action reads the background jobs a download may create, so "no job was created for this download" cannot be read. (1 spek)

**Verifikasi:** Luar filter. Semua spek di entri ini di luar filter, jadi tidak dibuatkan issue (aturan Filter).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-UCF-E2E-058` | GlobalSettings / CustomFieldUser | Download di Atas 5.000 Baris Tabel Custom Field: Loading Screen sampai Berkas Siap lalu Langsung Te… | Medium / Edge | Luar | Lolos tak lengkap |

### Tema: 1) the retention is written only by Admin Console PATCH /v2/enterprise-management/lifecycle-settings/recycle-bin, a platform-wide Principal setting t… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager nyata (set Upload Date / Deleted Date file uji); belum ada baris BT. Sesi gs mencatat satu BT untuk semua entri ini.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-029` | GlobalSettings / FileManager | Retensi Recycle Bin: Teks Info dan Kolom Auto-Purge In Mengikuti Lifecycle Settings | High / Edge | Dalam | Lolos tak lengkap |

### Tema: Auto-Purge In 29 days / 12 days / 1 day / 0 days — seedFileManagerRecycleBin soft-deletes every Tabel A3 row at the seeding time (all show 30 days) a… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager nyata (set Upload Date / Deleted Date file uji); belum ada baris BT. Sesi gs mencatat satu BT untuk semua entri ini.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-029` | GlobalSettings / FileManager | Retensi Recycle Bin: Teks Info dan Kolom Auto-Purge In Mengikuti Lifecycle Settings | High / Edge | Dalam | Lolos tak lengkap |

### Tema: Bayu Anggraini's Fixed Asset App Access revoked: the per-product status route (/v2/iam/users/products/{product}/status/bulk) has no body schema in th… (1 spek)

**Verifikasi:** Issue/helper sudah ada. Tercatat di BT-AUTH-SES-3 → `iam-service#184` (route status per produk). Bukan issue baru.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-057` | Auth / SessionManagement | Pencatatan Sesi karena App Access Dicabut, Admin Force-Logout, Change Password, Deactivate, dan Del… | High / Positive | Dalam | Lolos tak lengkap |

### Tema: Client User with Manage privacy policy assigned by mistake: the backend refuses it (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: backend menolak state ini, jadi state mustahil = spec defect, perlu D-entry Coordinator.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-PP-E2E-011` | AdminConsole / SettingsPrivacyPolicy | Role Matrix Negatif: Entity Gate Distributor, Partner, dan Client Tidak Mengakses Privacy Policy | Critical / Negative | Dalam | Lolos tak lengkap |

### Tema: Division "—": the create requires a Division (divisionId is required in user-crud.yaml UserBody), so no user without one can be made and Winarsih's r… (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: `divisionId` wajib di kontrak; butuh keputusan produk (Division opsional), bukan issue.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-LP-E2E-039` | Auth / LoginPassword | Kolom Entri Login pada Activity Log Session dan User Log | High / Positive | Dalam | Gagal |

### Tema: Hardware Stock > Stock List and Add Stock: Hardware Stock has no backend on the stack (sprint board item 40, no Create API), so its rows and SKU choi… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Basi: sprint board 19 Nov baris 40 (Hardware Stock) sudah ⚙️, dan API hardware-stock enterprise-management sudah dipakai (mis. `enterprise-management-service#305`). Sesi ac retag dari run terbaru.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-DS-E2E-154` | AdminConsole / SettingsDeviceSku | Sinkron Modul Stok: Register SKU Hardware dan TAG Menjadi Pilihan Add Stock dan Baris Stock List | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: Hardware Stock > Stock List and Stock Detail: Hardware Stock has no backend on the stack (sprint board item 40, no Create API) (1 spek)

**Verifikasi:** Basi atau sudah selesai. Basi: sprint board 19 Nov baris 40 (Hardware Stock) sudah ⚙️, dan API hardware-stock enterprise-management sudah dipakai (mis. `enterprise-management-service#305`). Sesi ac retag dari run terbaru.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-DS-E2E-155` | AdminConsole / SettingsDeviceSku | Sinkron Modul Stok: Edit Brand, Model/Type, Photo, dan Device Name Tercermin pada Stock List dan St… | High / Positive | Dalam | Lolos tak lengkap |

### Tema: Hardware Stock > Stock List and its Device Name filter: Hardware Stock has no backend on the stack (sprint board item 40, no Create API) (1 spek)

**Verifikasi:** Basi atau sudah selesai. Basi: sprint board 19 Nov baris 40 (Hardware Stock) sudah ⚙️, dan API hardware-stock enterprise-management sudah dipakai (mis. `enterprise-management-service#305`). Sesi ac retag dari run terbaru.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-DS-E2E-155` | AdminConsole / SettingsDeviceSku | Sinkron Modul Stok: Edit Brand, Model/Type, Photo, dan Device Name Tercermin pada Stock List dan St… | High / Positive | Dalam | Lolos tak lengkap |

### Tema: Hendra enables a permission on System Role Role Uji {runId}-038: no System Role permission operation in plans/global-settings-role/api-contracts.json… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kontrak role tidak punya operasi permission System Role; belum ada baris BT. Sesi gs cek LLD role dulu.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-ACTLOG-E2E-038` | GlobalSettings / ActivityLog | Aksi Lain di User Action: Edit Permission System Role, Activate/Deactivate, Import | High / Positive | Dalam | Lolos tak lengkap |

### Tema: Kontrak Auth tidak punya operasi Create Session (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kontrak auth tanpa operasi Create Session; belum ada baris BT. Sesi ac.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-069` | Auth / SessionManagement | Absence Pencatatan: Penolakan Server, Force-logout Idempotent, dan Aksi Admin | Critical / Negative | Dalam | Lolos tak lengkap |

### Tema: Rina's own current photo as a File Manager file: same seed gap as TC-106 (T2-3); no BT row Helpers now exist: Spectra.setUserProfilePicture(userId) m… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Helper sudah ada (`Spectra.setUserProfilePicture`, `seedFileManagerFile({ userId })`, lihat label penyebab); skrip File Manager belum memakainya. Kelas (d), pemilik suite gs; bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-027` | GlobalSettings / FileManager | Auto-Transition: Ganti dan Hapus Foto Profil (User, My Profile, Non-Login User) Memindahkan Foto La… | Critical / Positive | Dalam | Gagal |

### Tema: Search GB finds big-banner.png (1.5 GB) — no route uploads a file of that size; seedFileManagerPreSetup uploads it as 1 KB, so no row shows GB (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager (file uji berukuran besar tanpa upload nyata); belum ada baris BT. Sesi gs.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-031` | GlobalSettings / FileManager | Search Tabel Utama: Siklus Toolbar, Substring, Case-Insensitive, Size, Trim, dan Karakter Khusus | High / Positive | Dalam | Lolos tak lengkap |

### Tema: TC-AUTH-SES-E2E-069 the Fixed Asset product status of a user switched back on: POST /v2/iam/users/products/{product}/status/bulk has no body in this… (1 spek)

**Verifikasi:** Issue/helper sudah ada. Tercatat di BT-AUTH-SES-3 → `iam-service#184` (route status per produk). Bukan issue baru.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-069` | Auth / SessionManagement | Absence Pencatatan: Penolakan Server, Force-logout Idempotent, dan Aksi Admin | Critical / Negative | Dalam | Lolos tak lengkap |

### Tema: TC-AUTH-SES-E2E-070 the BIOPOL profile and the unresolvable active Privacy Policy version (BE fixture; no action) (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan fixture BE (profil BIOPOL dan versi Privacy Policy aktif yang tak bisa di-resolve); belum ada baris BT. Sesi ac.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-070` | Auth / SessionManagement | Absence Pencatatan Biometric: Kondisi Re-login, Enroll, dan Disable yang Tidak Menulis Session Log… | High / Negative | Dalam | Lolos tak lengkap |

### Tema: TC-GS-FILEMGR-E2E-058 to 14 actor 'Agus Wibowo {runId}-058' deleted through DELETE /v2/iam/users after acting on 'stale-avatar' and 'expired-avatar':… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Helper sudah ada (`Spectra.setUserProfilePicture`, `seedFileManagerFile({ userId })`, lihat label penyebab); skrip File Manager belum memakainya. Kelas (d), pemilik suite gs; bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-058` | GlobalSettings / FileManager | Pencatatan Log: Snapshot Nama Aktor setelah Rename dan Hapus Akun, serta Entri Delete User | Medium / Edge | Dalam | Lolos tak lengkap |

### Tema: TC-GS-FILEMGR-E2E-058 to 18 user 'Dewi Kartika {runId}-058' with files, deleted through DELETE /v2/iam/users, its Changelog User row read through cha… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Helper sudah ada (`Spectra.setUserProfilePicture`, `seedFileManagerFile({ userId })`, lihat label penyebab); skrip File Manager belum memakainya. Kelas (d), pemilik suite gs; bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-058` | GlobalSettings / FileManager | Pencatatan Log: Snapshot Nama Aktor setelah Rename dan Hapus Akun, serta Entri Delete User | Medium / Edge | Dalam | Lolos tak lengkap |

### Tema: TC-GS-FILEMGR-E2E-058 to 6 a seeded actor who deletes files, then is renamed: the pieces exist (seedLoginUser, fileManagerSeedRecycledFile deletedBy,… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Helper sudah ada (`Spectra.setUserProfilePicture`, `seedFileManagerFile({ userId })`, lihat label penyebab); skrip File Manager belum memakainya. Kelas (d), pemilik suite gs; bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-058` | GlobalSettings / FileManager | Pencatatan Log: Snapshot Nama Aktor setelah Rename dan Hapus Akun, serta Entri Delete User | Medium / Edge | Dalam | Lolos tak lengkap |

### Tema: TC-GS-FILEMGR-E2E-059 to 12 'budi-avatar-{runId}-059.jpg' with Upload Date 02/09/26 14:30: the upload time is the server's clock and no route sets a… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager nyata (set Upload Date / Deleted Date file uji); belum ada baris BT. Sesi gs mencatat satu BT untuk semua entri ini.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-059` | GlobalSettings / FileManager | Format Tanggal dan Waktu General Settings pada Upload Date, Deleted Date, Date Changelog, dan Input… | High / Positive | Dalam | Lolos tak lengkap |

### Tema: TC-GS-FILEMGR-E2E-059 to 17 'old-avatar-{runId}-059.png' with a seeded Deleted Date: fileManagerSeedRecycledFile deletes at the server's clock and no… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager nyata (set Upload Date / Deleted Date file uji); belum ada baris BT. Sesi gs mencatat satu BT untuk semua entri ini.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-059` | GlobalSettings / FileManager | Format Tanggal dan Waktu General Settings pada Upload Date, Deleted Date, Date Changelog, dan Input… | High / Positive | Dalam | Lolos tak lengkap |

### Tema: TC-GS-FILEMGR-E2E-062 to 36 Client status Expired: setTestTenantStatus (PATCH …/dev/clients/{clientCode}/status) accepts only 'Active' and 'Suspended… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper ems (`setTestTenantStatus` hanya Active/Suspended; belum ada status Expired); belum ada baris BT. Sesi gs.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-062` | GlobalSettings / FileManager | State Tenant: Aksi Tulis Ditolak saat Client Suspended atau Expired | High / Negative | Dalam | Lolos tak lengkap |

### Tema: TC-GS-FILEMGR-E2E-064 'expired-avatar-{runId}-064.jpg' deleted 31 days ago: fileManagerSeedRecycledFile puts it in the Recycle Bin, but no route sets… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager nyata (set Upload Date / Deleted Date file uji); belum ada baris BT. Sesi gs mencatat satu BT untuk semua entri ini.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-064` | GlobalSettings / FileManager | State Tenant: Auto-Purge dan Cascade Purge Tetap Berjalan saat Client Suspended | High / Edge | Dalam | Lolos tak lengkap |

### Tema: TC-GS-FILEMGR-E2E-064 to 15 the real user 'Dewi Kartika {runId}-064' owning an active photo and a Recycle Bin copy, deleted through DELETE /v2/iam/us… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Helper sudah ada (`Spectra.setUserProfilePicture`, `seedFileManagerFile({ userId })`, lihat label penyebab); skrip File Manager belum memakainya. Kelas (d), pemilik suite gs; bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-064` | GlobalSettings / FileManager | State Tenant: Auto-Purge dan Cascade Purge Tetap Berjalan saat Client Suspended | High / Edge | Dalam | Lolos tak lengkap |

### Tema: TC-GS-FILEMGR-E2E-064 to 7 a run of the daily file auto-purge job while Suspended: triggerSchedule runs only the iam schedules ('idle-expire', 'otp-p… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager (pemicu job auto-purge / injeksi gagal storage); belum ada baris BT. Sesi gs.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-064` | GlobalSettings / FileManager | State Tenant: Auto-Purge dan Cascade Purge Tetap Berjalan saat Client Suspended | High / Edge | Dalam | Lolos tak lengkap |

### Tema: Upload Date 02/09/26 14:30 — no route sets a file's upload time; seedFileManagerPreSetup uploads at the seed time (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager nyata (set Upload Date / Deleted Date file uji); belum ada baris BT. Sesi gs mencatat satu BT untuk semua entri ini.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-001` | GlobalSettings / FileManager | Screening Tabel Utama File Manager: Layout, Urutan Default, Row Action, dan Tooltip | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: Upload Dates 01/09/26 and 02/09/26 (siti-profile.png, budi-avatar.jpg) — no route sets a file's upload time; every Tabel A2 row carries the seeding t… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager nyata (set Upload Date / Deleted Date file uji); belum ada baris BT. Sesi gs mencatat satu BT untuk semua entri ini.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-033` | GlobalSettings / FileManager | Filter Tabel Utama: Multi-Select OR, Rentang Size, Rentang Upload Date, dan Logika AND | High / Positive | Dalam | Lolos tak lengkap |

### Tema: Upload Dates 02/09/26 14:30, 01/09/26 09:00, 20/08/26 10:15 — no route sets a file's upload time; the seed uploads oldest first, so only the order is… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager nyata (set Upload Date / Deleted Date file uji); belum ada baris BT. Sesi gs mencatat satu BT untuk semua entri ini.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-001` | GlobalSettings / FileManager | Screening Tabel Utama File Manager: Layout, Urutan Default, Row Action, dan Tooltip | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: a Non-Login User whose photo is a File Manager file, deleted through DELETE /v2/iam/non-login-users/{id}: same seed gap (T2-3); no BT row Helpers now… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Helper sudah ada (`Spectra.setUserProfilePicture`, `seedFileManagerFile({ userId })`, lihat label penyebab); skrip File Manager belum memakainya. Kelas (d), pemilik suite gs; bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-028` | GlobalSettings / FileManager | Cascade Purge: Delete User dan Non-Login User Menghapus Permanen Seluruh File | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: a Non-Login User whose photo is a File Manager file: same seed gap as TC-106 (T2-3; the non-login user photo is set through its own feature API); no… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Helper sudah ada (`Spectra.setUserProfilePicture`, `seedFileManagerFile({ userId })`, lihat label penyebab); skrip File Manager belum memakainya. Kelas (d), pemilik suite gs; bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-027` | GlobalSettings / FileManager | Auto-Transition: Ganti dan Hapus Foto Profil (User, My Profile, Non-Login User) Memindahkan Foto La… | Critical / Positive | Dalam | Gagal |

### Tema: a Temporary-expired Non-Login User: ageTime (scope users) did not move his Temporary Until into the past (1 spek)

**Verifikasi:** Luar filter. Semua spek di entri ini di luar filter, jadi tidak dibuatkan issue (aturan Filter).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-NLU-E2E-073` | GlobalSettings / NonLoginUser | Auto-Deactivate Temporary User oleh Sistem dan Cascade Purge Foto | High / Edge | Luar | Gagal |

### Tema: a Total Control Principal with no SKU and no Changelog (; only one Principal per backend: Fixture.settingsDeviceSku.notSeedable.otherPrincipals) (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: Principal hanya satu per backend (`ensurePrincipalTenant`), spec tanpa tag `principal` tidak memakainya. Butuh keputusan Coordinator (tag atau spec defect), bukan issue.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-DS-E2E-095` | AdminConsole / SettingsDeviceSku | Filter List: Opsi Ter-update setelah Register, State Loading Dropdown, dan No options available | Medium / Edge | Luar | Gagal |

### Tema: a cascade purge whose first storage delete fails and is retried: no test-only route injects a storage failure (and the real-owner seed of T2-3); no B… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Helper sudah ada (`Spectra.setUserProfilePicture`, `seedFileManagerFile({ userId })`, lihat label penyebab); skrip File Manager belum memakainya. Kelas (d), pemilik suite gs; bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-028` | GlobalSettings / FileManager | Cascade Purge: Delete User dan Non-Login User Menghapus Permanen Seluruh File | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: a failure of the sign-in alert mail alone — needs a fault route for the alert channel (Mailpit chaos, setMailFailure, fails every delivery, the OTP m… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper (gagal kirim hanya untuk kanal alert); belum ada baris BT. Sesi ac.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-MFA-E2E-048` | Auth / Mfa | Resilience Kegagalan Verifikasi Enrollment dan Pengiriman Email Alert | High / Negative | Dalam | Gagal |

### Tema: a file deleted 31 days ago (retention 30) must be purged by the daily auto-purge job; the job has no trigger in this suite and no route ages a file's… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager nyata (set Upload Date / Deleted Date file uji); belum ada baris BT. Sesi gs mencatat satu BT untuk semua entri ini.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-030` | GlobalSettings / FileManager | Auto-Purge Job: Batas Retensi Inklusif, Floor 48 Jam, Retry, dan Balapan dengan Permanently Delete | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: a seeded user deleted through the feature API: DELETE /v2/iam/users exists wrapped by Spectra.deleteUsers, and the cascade checks of this spec need r… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Helper sudah ada (`Spectra.setUserProfilePicture`, `seedFileManagerFile({ userId })`, lihat label penyebab); skrip File Manager belum memakainya. Kelas (d), pemilik suite gs; bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-028` | GlobalSettings / FileManager | Cascade Purge: Delete User dan Non-Login User Menghapus Permanen Seluruh File | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: a storage delete that fails on the first job run and succeeds on the next needs a storage-failure fixture and the auto-purge job trigger; neither exi… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager (pemicu job auto-purge / injeksi gagal storage); belum ada baris BT. Sesi gs.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-030` | GlobalSettings / FileManager | Auto-Purge Job: Batas Retensi Inklusif, Floor 48 Jam, Retry, dan Balapan dengan Permanently Delete | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: a user whose current profile photo is a File Manager file: no seeded file is a real user's photo (integration-findings T2-3: the internal upload take… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Helper sudah ada (`Spectra.setUserProfilePicture`, `seedFileManagerFile({ userId })`, lihat label penyebab); skrip File Manager belum memakainya. Kelas (d), pemilik suite gs; bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-027` | GlobalSettings / FileManager | Auto-Transition: Ganti dan Hapus Foto Profil (User, My Profile, Non-Login User) Memindahkan Foto La… | Critical / Positive | Dalam | Gagal |

### Tema: a user's current photo to remove: same seed gap as TC-106 (T2-3; the removal is DELETE /v2/iam/users/{id}/profile-picture); no BT row Helpers now exi… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Helper sudah ada (`Spectra.setUserProfilePicture`, `seedFileManagerFile({ userId })`, lihat label penyebab); skrip File Manager belum memakainya. Kelas (d), pemilik suite gs; bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-027` | GlobalSettings / FileManager | Auto-Transition: Ganti dan Hapus Foto Profil (User, My Profile, Non-Login User) Memindahkan Foto La… | Critical / Positive | Dalam | Gagal |

### Tema: big-banner.png (1.5 GB) first in descending order — seedFileManagerPreSetup uploads it as a 1 KB placeholder, so it ties dewi-kartika.jpg (1 KB) at t… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager (file uji berukuran besar tanpa upload nyata); belum ada baris BT. Sesi gs.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-035` | GlobalSettings / FileManager | Sort Tabel Utama: Siklus 3 Tahap, Nama Lengkap, Nilai Byte, Perpindahan Kolom, dan Tie-Breaker | High / Positive | Dalam | Lolos tak lengkap |

### Tema: big-banner.png 1.5 GB — no route uploads a file of that size; seedFileManagerPreSetup uploads a 1 KB placeholder (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager (file uji berukuran besar tanpa upload nyata); belum ada baris BT. Sesi gs.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-002` | GlobalSettings / FileManager | Isi Sel Tabel Utama: File Format, Nama User, Format Size, Nama Panjang, dan Link File Name | High / Positive | Dalam | Lolos tak lengkap |

### Tema: exactly one new session for the user: no route lists a user's sessions (plans/auth/api-contracts.json has none; no BT row) (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper iam nyata (route uji yang membaca daftar sesi user); belum ada baris BT. Sesi ac mencatat satu BT untuk semua entri ini.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-011` | Auth / SessionManagement | Cancel, Escape, Backdrop, Klik Ganda Confirm, dan Confirm pada Dialog Duplicate Login Attempt di Web | Critical / Negative | Dalam | Lolos tak lengkap |

### Tema: files owned by the real user Dewi Kartika, purged by the cascade when the user is deleted: no seeded file belongs to a real user (T2-3); re-seed with… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Helper sudah ada (`Spectra.setUserProfilePicture`, `seedFileManagerFile({ userId })`, lihat label penyebab); skrip File Manager belum memakainya. Kelas (d), pemilik suite gs; bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-028` | GlobalSettings / FileManager | Cascade Purge: Delete User dan Non-Login User Menghapus Permanen Seluruh File | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: files owned by the users Dewi Kartika and Dewi Kusuma: the internal upload takes the owner from userId, so every seeded file's User Name is the suite… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Helper sudah ada (`Spectra.setUserProfilePicture`, `seedFileManagerFile({ userId })`, lihat label penyebab); skrip File Manager belum memakainya. Kelas (d), pemilik suite gs; bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-035` | GlobalSettings / FileManager | Sort Tabel Utama: Siklus 3 Tahap, Nama Lengkap, Nilai Byte, Perpindahan Kolom, dan Tie-Breaker | High / Positive | Dalam | Lolos tak lengkap |

### Tema: for Principal: the Principal tenant is the singleton ensurePrincipalTenant, which PROJECT.md reserves for specs tagged principal (this spec.md has no… (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: Principal hanya satu per backend (`ensurePrincipalTenant`), spec tanpa tag `principal` tidak memakainya. Butuh keputusan Coordinator (tag atau spec defect), bukan issue.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-ACTLOG-E2E-061` | GlobalSettings / ActivityLog | Log Lama Tanpa Batas Waktu untuk Client, Principal, Distributor, Partner | Medium / Edge | Dalam | Lolos tak lengkap |

### Tema: seeding Recycle Bin files at a relative Deleted Date (29 and 31 days ago), the 10-day retention change, and the daily auto-purge job trigger are not… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager nyata (set Upload Date / Deleted Date file uji); belum ada baris BT. Sesi gs mencatat satu BT untuk semua entri ini.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-030` | GlobalSettings / FileManager | Auto-Purge Job: Batas Retensi Inklusif, Floor 48 Jam, Retry, dan Balapan dengan Permanently Delete | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: the 1-day retention and the reset-countdown job of TC-20 (see above): a platform-wide Principal setting and no job trigger route (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager (pemicu job auto-purge / injeksi gagal storage); belum ada baris BT. Sesi gs.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-029` | GlobalSettings / FileManager | Retensi Recycle Bin: Teks Info dan Kolom Auto-Purge In Mengikuti Lifecycle Settings | High / Edge | Dalam | Lolos tak lengkap |

### Tema: the Auto-Purge In value 29 — seedFileManagerRecycleBin deletes at the seed time; no route sets a file's deletion time (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager nyata (set Upload Date / Deleted Date file uji); belum ada baris BT. Sesi gs mencatat satu BT untuk semua entri ini.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-052` | GlobalSettings / FileManager | Download Tabel Utama dan Export Lintas Surface: Isi File CSV dan XLSX, Nama File, dan Kolom Tersemb… | High / Positive | Dalam | Lolos tak lengkap |

### Tema: the File Manager and Recycle Bin file counts against the baseline of (1 spek)

**Verifikasi:** Luar filter. Semua spek di entri ini di luar filter, jadi tidak dibuatkan issue (aturan Filter).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-NLU-E2E-073` | GlobalSettings / NonLoginUser | Auto-Deactivate Temporary User oleh Sistem dan Cascade Purge Foto | High / Edge | Luar | Gagal |

### Tema: the Principal tenant's user (Wulan Santoso): ensurePrincipalTenant exists, but the Principal is a singleton only specs with tags: [principal] in spec… (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: Principal hanya satu per backend (`ensurePrincipalTenant`), spec tanpa tag `principal` tidak memakainya. Butuh keputusan Coordinator (tag atau spec defect), bukan issue.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-MFA-E2E-040` | Auth / Mfa | Paritas MFA untuk User Entitas Distributor, Partner, dan Principal | Medium / Positive | Luar | Gagal |

### Tema: the TAG BYO row that keeps the snapshot Snap Tag Co {runId}-065 (Brand deleted in ): All Tags reads its mock data source and no test route activates… (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: Global Settings > All Tags masih membaca MockDataSource (belum Connect API). Pemilik: Integration B.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-BRAND-E2E-065` | GlobalSettings / Brand | Sinkronisasi Brand ke All Tags: Pemilih Brand Activate TAG BYO dan Snapshot Nama Brand pada TAG | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: the Total Control Principal with no SKU : only one Principal tenant exists per backend (PROJECT.md, ensurePrincipalTenant), and the suite's holds the… (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: Principal hanya satu per backend (`ensurePrincipalTenant`), spec tanpa tag `principal` tidak memakainya. Butuh keputusan Coordinator (tag atau spec defect), bukan issue.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-DS-E2E-008` | AdminConsole / SettingsDeviceSku | State List: Loading, Empty State Principal Tanpa SKU, No Result, dan SKU Stok 0 Tetap Tampil | High / Positive | Dalam | Lolos tak lengkap |

### Tema: the Upload Date value 02/09/26 14:30 — seedFileManagerPreSetup uploads at the seed time; no route sets a file's upload time (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager nyata (set Upload Date / Deleted Date file uji); belum ada baris BT. Sesi gs mencatat satu BT untuk semua entri ini.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-052` | GlobalSettings / FileManager | Download Tabel Utama dan Export Lintas Surface: Isi File CSV dan XLSX, Nama File, dan Kolom Tersemb… | High / Positive | Dalam | Lolos tak lengkap |

### Tema: the Upload Date value 9/2/26 02:30 PM — seedFileManagerPreSetup uploads at the seed time; no route sets a file's upload time (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager nyata (set Upload Date / Deleted Date file uji); belum ada baris BT. Sesi gs mencatat satu BT untuk semua entri ini.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-052` | GlobalSettings / FileManager | Download Tabel Utama dan Export Lintas Surface: Isi File CSV dan XLSX, Nama File, dan Kolom Tersemb… | High / Positive | Dalam | Lolos tak lengkap |

### Tema: the auto-purge job must run while the Permanently Delete dialog is open; the job has no trigger in this suite, so the race cannot be set up. (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager (pemicu job auto-purge / injeksi gagal storage); belum ada baris BT. Sesi gs.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-030` | GlobalSettings / FileManager | Auto-Purge Job: Batas Retensi Inklusif, Floor 48 Jam, Retry, dan Balapan dengan Permanently Delete | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: the clone owner's photo unchanged: no seeded File Manager file is a real user's profile photo (integration-findings T2-3); re-seed with real owners t… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Helper sudah ada (`Spectra.setUserProfilePicture`, `seedFileManagerFile({ userId })`, lihat label penyebab); skrip File Manager belum memakainya. Kelas (d), pemilik suite gs; bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-015` | GlobalSettings / FileManager | Resilience Tulis: Delete Single, Bulk Delete, Permanently Delete, Storage Tidak Terjangkau, dan Gan… | High / Negative | Dalam | Lolos tak lengkap |

### Tema: the count of Nazar's active sessions — needs a route that lists a user's sessions (none in auth/session-management or PROJECT.md test routes; no BT r… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper iam nyata (route uji yang membaca daftar sesi user); belum ada baris BT. Sesi ac mencatat satu BT untuk semua entri ini.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-MFA-E2E-031` | Auth / Mfa | Trust Device dan Pencatatan Pasca Login Final MFA | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: the end of the Admin Console and Global Settings product sessions when the platform session expires: no route in PROJECT.md or plans/auth/api-contrac… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper iam (akhir sesi produk saat sesi platform habis); belum ada baris BT. Sesi ac.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-032` | Auth / SessionManagement | Admin Console dan Global Settings Tanpa Evaluasi Concurrent dan Tanpa Seat | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: the exact row sets — big-banner.png (1.5 GB) is seeded as a 1 KB placeholder (seedFileManagerPreSetup), so it falls in the 1 KB ranges and not in 102… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager (file uji berukuran besar tanpa upload nyata); belum ada baris BT. Sesi gs.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-033` | GlobalSettings / FileManager | Filter Tabel Utama: Multi-Select OR, Rentang Size, Rentang Upload Date, dan Logika AND | High / Positive | Dalam | Lolos tak lengkap |

### Tema: the expiresAt of the second heartbeat — same gap as (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: `expiresAt` dari jam server tidak bisa dicocokkan matcher `shouldHaveResponseBody` (kelas e, sesi testspectra).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-015` | Auth / SessionManagement | Heartbeat dan Sinyal Aktivitas Web | High / Positive | Dalam | Lolos tak lengkap |

### Tema: the expiresAt of the third heartbeat — same gap as (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: `expiresAt` dari jam server tidak bisa dicocokkan matcher `shouldHaveResponseBody` (kelas e, sesi testspectra).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-015` | Auth / SessionManagement | Heartbeat dan Sinyal Aktivitas Web | High / Positive | Dalam | Lolos tak lengkap |

### Tema: the first heartbeat answer's expiresAt (last activity + 15 minutes): expiresAt is a timestamp computed from the server clock, and a response body is… (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: `expiresAt` dari jam server tidak bisa dicocokkan matcher `shouldHaveResponseBody` (kelas e, sesi testspectra).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-015` | Auth / SessionManagement | Heartbeat dan Sinyal Aktivitas Web | High / Positive | Dalam | Lolos tak lengkap |

### Tema: the heartbeat answer's expiresAt (last activity + 15 minutes): expiresAt is a timestamp computed from the server clock, and a response body is matche… (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: `expiresAt` dari jam server tidak bisa dicocokkan matcher `shouldHaveResponseBody` (kelas e, sesi testspectra).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-015` | Auth / SessionManagement | Heartbeat dan Sinyal Aktivitas Web | High / Positive | Dalam | Lolos tak lengkap |

### Tema: the heartbeat answer's expiresAt (last activity + the idle limit): expiresAt is a timestamp computed from the server clock, and a response body is ma… (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: `expiresAt` dari jam server tidak bisa dicocokkan matcher `shouldHaveResponseBody` (kelas e, sesi testspectra).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-015` | Auth / SessionManagement | Heartbeat dan Sinyal Aktivitas Web | High / Positive | Dalam | Lolos tak lengkap |

### Tema: the number of Eko Prasetyo's sessions: no route lists a user's sessions (plans/auth/api-contracts.json has none); no BT row yet (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper iam nyata (route uji yang membaca daftar sesi user); belum ada baris BT. Sesi ac mencatat satu BT untuk semua entri ini.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-MFA-E2E-018` | Auth / Mfa | Akses Halaman MFA dan Navigasi Browser | High / Negative | Dalam | Gagal |

### Tema: the page's reaction to that second request and "no extra session": the page reacts only to requests it sent itself, and the second one is sent by the… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper iam nyata (route uji yang membaca daftar sesi user); belum ada baris BT. Sesi ac mencatat satu BT untuk semua entri ini.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-013` | Auth / SessionManagement | Token Pra-autentikasi dan Sesi Lama Kedaluwarsa saat Confirm Duplicate Login | High / Negative | Dalam | Lolos tak lengkap |

### Tema: the per-product reactivation of Lestari Maulana in Fixed Asset: POST /v2/iam/users/products/{product}/status/bulk has no body in this repository (see… (1 spek)

**Verifikasi:** Issue/helper sudah ada. Tercatat di BT-AUTH-SES-3 → `iam-service#184` (route status per produk). Bukan issue baru.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-027` | Auth / SessionManagement | User Dinonaktifkan di Produk Fixed Asset: Pemutusan Sesi-Produk | High / Positive | Dalam | Lolos tak lengkap |

### Tema: the periodic session sweep switched off and back on: PROJECT.md has only POST /v2/iam/dev/schedules/idle-expire/trigger (run it now), no route pauses… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper iam nyata (baca expiry sesi tanpa memperpanjang / jeda sweep); belum ada baris BT. Sesi ac mencatat BT.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-013` | Auth / SessionManagement | Token Pra-autentikasi dan Sesi Lama Kedaluwarsa saat Confirm Duplicate Login | High / Negative | Dalam | Lolos tak lengkap |

### Tema: the photo storage state after a refused Create (no file kept, none permanent) (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan route uji yang membaca status penyimpanan foto setelah submit ditolak; belum ada baris BT. Sesi ac.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-DS-E2E-172` | AdminConsole / SettingsDeviceSku | Resilience Foto Staging: Submit atau Save Gagal setelah Foto di Staging Tidak Membuat Foto Permanen | High / Edge | Dalam | Lolos tak lengkap |

### Tema: the photo storage state of foto-b.png after a refused Save (no file kept, none permanent) (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan route uji yang membaca status penyimpanan foto setelah submit ditolak; belum ada baris BT. Sesi ac.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AC-DS-E2E-172` | AdminConsole / SettingsDeviceSku | Resilience Foto Staging: Submit atau Save Gagal setelah Foto di Staging Tidak Membuat Foto Permanen | High / Edge | Dalam | Lolos tak lengkap |

### Tema: the pre-auth session's resend count: no route reads it (the OTP entry answers only cooldownSeconds and isResendExhausted); no BT row yet (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper iam nyata (baca penghitung pre-auth MFA); belum ada baris BT. Sesi ac mencatat satu BT.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-MFA-E2E-006` | Auth / Mfa | Siklus Resend OTP dan Cooldown 60 Detik | High / Positive | Dalam | Lolos tak lengkap |

### Tema: the retention change to 45 days and the reset-countdown job of TC-20 (see above): a platform-wide Principal setting and no job trigger route (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager (pemicu job auto-purge / injeksi gagal storage); belum ada baris BT. Sesi gs.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-029` | GlobalSettings / FileManager | Retensi Recycle Bin: Teks Info dan Kolom Auto-Purge In Mengikuti Lifecycle Settings | High / Edge | Dalam | Lolos tak lengkap |

### Tema: the session's expiresAt not extended by the close and reopen: no route reads a session's expiry without extending it (the heartbeat answers expiresAt… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper iam nyata (baca expiry sesi tanpa memperpanjang / jeda sweep); belum ada baris BT. Sesi ac mencatat BT.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-018` | Auth / SessionManagement | Refresh pada Dialog Session Expired dan Browser Dibuka Ulang | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: the session's expiresAt on the backend: no route reads a session's expiry without extending it (the heartbeat answers it but also extends it), and th… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper iam nyata (baca expiry sesi tanpa memperpanjang / jeda sweep); belum ada baris BT. Sesi ac mencatat BT.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-SES-E2E-015` | Auth / SessionManagement | Heartbeat dan Sinyal Aktivitas Web | High / Positive | Dalam | Lolos tak lengkap |

### Tema: the signed-in user's own profile photo as a File Manager file: same seed gap as TC-106 (T2-3; re-seed with real owners through the profile-picture AP… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Helper sudah ada (`Spectra.setUserProfilePicture`, `seedFileManagerFile({ userId })`, lihat label penyebab); skrip File Manager belum memakainya. Kelas (d), pemilik suite gs; bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-027` | GlobalSettings / FileManager | Auto-Transition: Ganti dan Hapus Foto Profil (User, My Profile, Non-Login User) Memindahkan Foto La… | Critical / Positive | Dalam | Gagal |

### Tema: the two TAG BYO rows (Brand Rename Tag Co {runId}-065): Global Settings > All Tags reads its mock data source (packages/features/global-settings-tag… (1 spek)

**Verifikasi:** Bukan BE. Bukan BE: Global Settings > All Tags masih membaca MockDataSource (belum Connect API). Pemilik: Integration B.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-BRAND-E2E-065` | GlobalSettings / Brand | Sinkronisasi Brand ke All Tags: Pemilih Brand Activate TAG BYO dan Snapshot Nama Brand pada TAG | Critical / Positive | Dalam | Lolos tak lengkap |

### Tema: the user's photos in File Manager and its Recycle Bin: no action seeds or reads a Non-Login User's photo files there (1 spek)

**Verifikasi:** Luar filter. Semua spek di entri ini di luar filter, jadi tidak dibuatkan issue (aturan Filter).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-NLU-E2E-073` | GlobalSettings / NonLoginUser | Auto-Deactivate Temporary User oleh Sistem dan Cascade Purge Foto | High / Edge | Luar | Gagal |

### Tema: the wrong-attempt count of Yuni Wijaya's pre-auth session one above the baseline: no route reads it (POST /v2/iam/auth/mfa/state answers no counter);… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper iam nyata (baca penghitung pre-auth MFA); belum ada baris BT. Sesi ac mencatat satu BT.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-MFA-E2E-013` | Auth / Mfa | Admin Reset Authenticator Saat Login MFA | High / Positive | Dalam | Gagal |

### Tema: the wrong-attempt count of Yuni Wijaya's pre-auth session: no route reads it (POST /v2/iam/auth/mfa/state answers no counter); no BT row yet (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper iam nyata (baca penghitung pre-auth MFA); belum ada baris BT. Sesi ac mencatat satu BT.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-MFA-E2E-013` | Auth / Mfa | Admin Reset Authenticator Saat Login MFA | High / Positive | Dalam | Gagal |

### Tema: the wrong-attempt counter of the pre-auth session — needs a route that reads it (POST /v2/iam/auth/mfa/state carries no counter; none in PROJECT.md;… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper iam nyata (baca penghitung pre-auth MFA); belum ada baris BT. Sesi ac mencatat satu BT.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-AUTH-MFA-E2E-043` | Auth / Mfa | Defense-in-Depth: Purpose OTP Lintas Login with OTP dan MFA serta Email Tujuan OTP | High / Negative | Dalam | Lolos tak lengkap |

### Tema: to 13 the clone owners' photos (Alexander Graham Bell emptied, Gita Lestari unchanged): no seeded File Manager file is a real user's profile photo (i… (1 spek)

**Verifikasi:** Basi atau sudah selesai. Helper sudah ada (`Spectra.setUserProfilePicture`, `seedFileManagerFile({ userId })`, lihat label penyebab); skrip File Manager belum memakainya. Kelas (d), pemilik suite gs; bukan issue BE.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-020` | GlobalSettings / FileManager | Bulk Delete Berhasil: Campuran, Seleksi Direset, dan Pindah ke Halaman Terakhir | Critical / Positive | Dalam | Gagal |

### Tema: to 17 the 1,001 Recycle Bin files and the raised Selection Limit of TC-88 (see above) (1 spek)

**Verifikasi:** Luar filter. Semua spek di entri ini di luar filter, jadi tidak dibuatkan issue (aturan Filter).

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-021` | GlobalSettings / FileManager | Bulk Delete dan Bulk Permanently Delete dengan 1.001 Baris Terseleksi | Medium / Edge | Luar | Lolos tak lengkap |

### Tema: to 62 a storage that cannot be reached during a Permanently Delete (and restored): no test-only route in PROJECT.md makes the file storage fail, and… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper file-manager (pemicu job auto-purge / injeksi gagal storage); belum ada baris BT. Sesi gs.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-015` | GlobalSettings / FileManager | Resilience Tulis: Delete Single, Bulk Delete, Permanently Delete, Storage Tidak Terjangkau, dan Gan… | High / Negative | Dalam | Lolos tak lengkap |

### Tema: to 72 a photo replacement whose soft-delete of the old photo fails inside the backend (the backend rolls back): no test-only route in PROJECT.md inje… (1 spek)

**Verifikasi:** Kebutuhan BE nyata, belum ada ID BT. Kebutuhan helper (injeksi gagal soft-delete foto lama); belum ada baris BT. Sesi gs.

| Spek | Suite | Judul | Prioritas | Filter | Status |
|---|---|---|---|---|---|
| `TC-GS-FILEMGR-E2E-015` | GlobalSettings / FileManager | Resilience Tulis: Delete Single, Bulk Delete, Permanently Delete, Storage Tidak Terjangkau, dan Gan… | High / Negative | Dalam | Lolos tak lengkap |

## Gagal saat run, belum ada temuan BT (22 spek)

Spek ini gagal karena API BE menolak request, tapi penyebabnya belum dicatat sebagai temuan BT. Kolom Error berisi pesan dari run terakhir.

| Spek | Judul | Prioritas | Filter | Status | Error singkat | Verifikasi |
|---|---|---|---|---|---|---|
| `TC-AC-ACC-E2E-149` (Client) | Delete Client Archived: Dialog Konfirmasi D-05 dan Warning D-04, Tombol Delete Disabled S… | Critical / Positive | Dalam | Gagal | PATCH /v2/iam/users/905019724100064 answered 422: {"message":"Invalid request body","error":[{"field":"access","message":"Access… | Skrip (d), sesi ac: body PATCH user dibentuk dari kontrak/DTO, bukan dari respons baca. |
| `TC-AUTH-OTP-E2E-005` (LoginOtp) | Akses Langsung ke Layar Login with OTP tanpa Sesi dan Pengalihan bagi Pengguna yang Sudah… | High / Edge | Luar | Gagal | POST /v2/iam/products/global_settings/roles/access-level answered 403: {"message":"Forbidden","data":{"reason":"entity_type"}} Ex… | Luar filter. |
| `TC-AUTH-OTP-E2E-016` (LoginOtp) | Verify OTP Berhasil Langsung ke Product Hub tanpa Agreement dan MFA | Critical / Positive | Dalam | Gagal | POST /v2/iam/products/global_settings/roles/access-level answered 403: {"message":"Forbidden","data":{"reason":"entity_type"}} | Skrip (d), sesi ac: 403 `entity_type` = aktor salah untuk route role Global Settings; setup pakai aktor tenant yang benar. |
| `TC-AUTH-LP-E2E-036` (LoginPassword) | Pencatatan Log Tahap Lock 15 Menit, 1 Jam, dan Requires Reset | Critical / Positive | Dalam | Gagal | POST /v2/iam/dev/time/age answered 500: {"message":"age public.login_attempt_locks: ERROR: duplicate key value violates unique co… | Helper BE (c), sesi ac: route uji `POST /v2/iam/dev/time/age` 500 duplicate key di `login_attempt_locks`. Belum ada baris BT; catat BT dengan request asli. |
| `TC-AUTH-LP-E2E-052` (LoginPassword) | Password Benar Mengatur Ulang Data Lock Harian Tanpa Mengubah Hitungan Hari Berturut-turut | High / Edge | Luar | Gagal | POST /v2/iam/dev/time/age answered 500: {"message":"age public.login_attempt_locks: ERROR: duplicate key value violates unique co… | Luar filter (penyebab sama dengan LP-036). |
| `TC-AUTH-MFA-E2E-013` (Mfa) | Admin Reset Authenticator Saat Login MFA | High / Positive | Dalam | Gagal | POST /v2/iam/products/global_settings/roles/access-level answered 403: {"message":"Forbidden","data":{"reason":"entity_type"}} Th… | Skrip (d), sesi ac: sama dengan OTP-016 (403 `entity_type`). |
| `TC-AUTH-MFA-E2E-018` (Mfa) | Akses Halaman MFA dan Navigasi Browser | High / Negative | Dalam | Gagal | POST /v2/iam/products/global_settings/roles/access-level answered 403: {"message":"Forbidden","data":{"reason":"entity_type"}} | Skrip (d), sesi ac: sama dengan OTP-016 (403 `entity_type`). |
| `TC-FA-GRP-E2E-159` (SettingsGroups) | Modal Changelog Kolom Group Name: Full Path Subgroup, Path Setelah Rename, Snapshot Tidak… | High / Positive | Dalam | Gagal | PATCH /v2/iam/groups/fixed_asset/{id} answered 422: {"message":"Invalid request body","error":[{"field":"description","message":"… | Skrip (d), sesi fai: body PATCH group 422; bentuk dari kontrak. |
| `TC-FA-GRP-E2E-163` (SettingsGroups) | Tab Users Search per Kolom Activation Status, Temporary User, TAG, dan Custom Field | High / Positive | Dalam | Gagal | listCustomFields: answered 403: {"message":"Forbidden","data":{"reason":"capability"}} | Bukan BE, sesi fai: 403 `capability` di `listCustomFields`; BT-FA-GRP-11 ditolak, pakai `GET /v2/iam/user-custom-fields/dropdown`. |
| `TC-FA-GRP-E2E-165` (SettingsGroups) | Tab Users Filter: Screening Panel dan Filter Position (Isi Opsi, Satu/Dua Opsi OR, Search… | High / Positive | Dalam | Gagal | listCustomFields: answered 401: {"message":"Unauthorized","reason":"duplicate_login"} | Skrip (d), sesi fai: 401 `duplicate_login` = login ganda aktor yang sama di run paralel. |
| `TC-FA-GRP-E2E-170` (SettingsGroups) | Tab Users Filter Temporary User (Yes/No), Temporary Until (Rentang), dan Custom Field Dro… | High / Positive | Dalam | Gagal | listCustomFields: answered 403: {"message":"Forbidden","data":{"reason":"capability"}} | Bukan BE, sesi fai: 403 `capability` di `listCustomFields`; BT-FA-GRP-11 ditolak, pakai `GET /v2/iam/user-custom-fields/dropdown`. |
| `TC-FA-GRP-E2E-171` (SettingsGroups) | Tab Users Filter Custom Field Multi-Dropdown dan Date serta Kombinasi AND (Group Role + A… | High / Positive | Dalam | Gagal | listCustomFields: answered 403: {"message":"Forbidden","data":{"reason":"capability"}} | Bukan BE, sesi fai: 403 `capability` di `listCustomFields`; BT-FA-GRP-11 ditolak, pakai `GET /v2/iam/user-custom-fields/dropdown`. |
| `TC-FA-GRP-E2E-176` (SettingsGroups) | Tab Users Sort Kolom TAG, Custom Field, dan Nilai Kosong (Akhir Asc, Awal Desc, Tie-Break… | High / Positive | Dalam | Gagal | listCustomFields: answered 403: {"message":"Forbidden","data":{"reason":"capability"}} | Bukan BE, sesi fai: 403 `capability` di `listCustomFields`; BT-FA-GRP-11 ditolak, pakai `GET /v2/iam/user-custom-fields/dropdown`. |
| `TC-FA-GRP-E2E-178` (SettingsGroups) | Tab Users Setup Column: Screening Overlay dan Popup, Guard Kolom Terakhir, dan Pin ke-4 D… | High / Positive | Dalam | Gagal | listCustomFields: answered 403: {"message":"Forbidden","data":{"reason":"capability"}} | Bukan BE, sesi fai: 403 `capability` di `listCustomFields`; BT-FA-GRP-11 ditolak, pakai `GET /v2/iam/user-custom-fields/dropdown`. |
| `TC-FA-GRP-E2E-179` (SettingsGroups) | Tab Users Setup Column: Batas Max Visible Columns Kolom ke-21, [Reset to Default], (X) da… | High / Positive | Dalam | Gagal | listCustomFields: answered 403: {"message":"Forbidden","data":{"reason":"capability"}} | Bukan BE, sesi fai: 403 `capability` di `listCustomFields`; BT-FA-GRP-11 ditolak, pakai `GET /v2/iam/user-custom-fields/dropdown`. |
| `TC-FA-GRP-E2E-182` (SettingsGroups) | Tab Users Setup Column: Centang Kolom Curated Temporary User, Temporary Until, TAG, dan C… | High / Positive | Dalam | Gagal | listCustomFields: answered 403: {"message":"Forbidden","data":{"reason":"capability"}} | Bukan BE, sesi fai: 403 `capability` di `listCustomFields`; BT-FA-GRP-11 ditolak, pakai `GET /v2/iam/user-custom-fields/dropdown`. |
| `TC-FA-GRP-E2E-184` (SettingsGroups) | Tab Users Setup Column: Geser (Drag) Kolom Group Role, Activation Status, Temporary User,… | High / Positive | Dalam | Gagal | listCustomFields: answered 403: {"message":"Forbidden","data":{"reason":"capability"}} | Bukan BE, sesi fai: 403 `capability` di `listCustomFields`; BT-FA-GRP-11 ditolak, pakai `GET /v2/iam/user-custom-fields/dropdown`. |
| `TC-GS-DIV-E2E-072` (Division) | Import Create Missing Divisions: Master Data Count Limit dan Duplicate Race | High / Negative | Dalam | Gagal | importDraftJob userLogin: GET …/jobs answered 403: {"message":"Forbidden","data":{"reason":"plan_required"},"error":null} | Skrip (d), sesi gs: 403 `plan_required`, tenant uji belum punya plan yang memuat Import. |
| `TC-GS-IMPORT-E2E-100` (Import) | Edit Mode Tab User: pilihan Use untuk nilai baru, nilai tersimpan Invalid, all-or-nothing… | Critical / Positive | Dalam | Gagal | AutoComplete: expected hasOption() to be true, got false after 3000ms importDiscardDraft userLogin: DELETE …/jobs/{id} answered 4… | Bukan BE: kegagalan AutoComplete (opsi tidak muncul). Sesi gs triase sebagai skrip/UI. |
| `TC-GS-USER-E2E-110` (User) | Tab Non-Login User Detail: kombinasi Search dan Filter, Clear, filter kolom hidden, nol b… | Medium / Positive | Luar | Gagal | POST /v2/iam/non-login-users answered 422: {"message":"Invalid request body","error":[{"field":"customFields.Emergency Phone","me… | Luar filter. |
| `TC-GS-USER-E2E-111` (User) | Tab Non-Login User Detail: Sort 3-state, Pagination, dan kombinasi Search+Filter+Sort+Pag… | Medium / Positive | Luar | Gagal | POST /v2/iam/non-login-users answered 422: {"message":"Invalid request body","error":[{"field":"customFields.Emergency Phone","me… | Luar filter. |
| `TC-GS-USER-E2E-112` (User) | Tab Non-Login User Detail: Setup Column (overlay, popup, hide, reorder, pin, reset, guard) | Medium / Positive | Luar | Gagal | POST /v2/iam/non-login-users answered 422: {"message":"Invalid request body","error":[{"field":"customFields.Emergency Phone","me… | Luar filter. |

---
id: TC-GS-GSET-E2E-048-defense-in-depth-rbac-put-dan-get-langsung
title: "Direct API RBAC"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-124
  - TC-GS-GSET-125
  - TC-GS-GSET-126
  - TC-GS-GSET-127
  - TC-GS-GSET-128
  - TC-GS-GSET-129
  - TC-GS-GSET-130
coverage:
  web: automated
---

# Direct API RBAC

## Prerequisites

- Mode: FE+BE.
- Klien HTTP (disediakan tim FE) yang mengirim request langsung ke server, tanpa melewati browser, untuk `PUT` dan `GET /v2/enterprise-management/general-settings` (`API/openapi.yaml`), memakai token sesi aktor yang diperoleh lewat login API dengan kredensial dari env var. Penangkapan token disediakan tim FE. Spec ini hanya mengasersi respons server dan state data (bagian 8b butir 1); tidak ada asersi tampilan UI.
- Akun yang diuji (semua email dari Tabel Data Uji Pre-setup; sesi API dibuat di hook `before`):

  | Kode | Role | Email | Environment variable password |
  |---|---|---|---|
  | RO | Read Only (Pre-setup No 3) | `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `GS_GSET_RO_PASSWORD` (nama env baru) |
  | SR | System Role (Pre-setup No 5) | `noCapabilityGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `GS_GSET_SR_PASSWORD` (nama env baru) |
  | CI | Capability Individual (Pre-setup No 4) | `manageUserRoleRead_automated_{namaCompany}@qwertysystem.net` | `GS_GSET_CI_PASSWORD` (nama env baru) |
  | TC-A | Total Control Client A (Pre-setup No 1), pembaca nilai tersimpan | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `GS_TC_PASSWORD` |
  | TC-S | Total Control staf `Client Suspended` (Pre-setup No 16) | tidak tertulis di Pre-setup; disediakan tim FE (lihat Temuan untuk QA) | `GS_SUSPENDED_TC_PASSWORD` |

- Login UI akun default suite (TC-A) di hook `before` spec ini; hook `after` tidak perlu memulihkan sesi karena tidak ada ganti akun UI. Pergantian aktor pada langkah adalah pergantian token sesi API.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Environment variable: `GS_GSET_RO_PASSWORD`, `GS_GSET_SR_PASSWORD`, `GS_GSET_CI_PASSWORD`, `GS_TC_PASSWORD`, `GS_SUSPENDED_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Tiga nama `GS_GSET_*` adalah nama baru yang belum terdaftar di `executionConfig.environmentVariables` dan `.env.example` (didaftarkan pada tahap script).
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` dan pemulihan record Client A ke baseline Pre-setup No 10): lihat `suite.md`, bagian Hook suite; spec ini tidak mengatur flag sendiri.
- Data Pre-setup (read-only, tidak diubah karena semua PUT ditolak): record Client A pada baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`) dan record `Client Suspended` yang berstatus suspended (Pre-setup No 16) dengan Session Idle Timeout `30 minutes` (disediakan tim FE). Spec tidak membuat data dinamis.
- Payload PUT valid: `currencyCode` `IDR`, `timezone` `Asia/Jakarta`, `dateFormat` `dd/MM/yy`, `timeFormat` `HH:mm`, `sessionIdleTimeout` `60` (nilai tersimpan kecuali Session Idle Timeout).
- Tabel "PUT langsung" (dipakai langkah 1 sampai 6):

  | Urutan | TC | Aktor |
  |---|---|---|
  | 1 | TC-GS-GSET-124 | RO |
  | 2 | TC-GS-GSET-125 | SR |
  | 3 | TC-GS-GSET-126 | CI |

- Tabel "GET langsung" (dipakai langkah 7 sampai 11):

  | Urutan | TC | Aktor | Status | Isi respons |
  |---|---|---|---|---|
  | 1 | TC-GS-GSET-127 | SR | `403` `Forbidden` | tidak memuat nilai General Settings |
  | 2 | TC-GS-GSET-128 | CI | `403` `Forbidden` | tidak memuat nilai General Settings |
  | 3 | TC-GS-GSET-129 | RO | `200` | `currencyCode` `IDR`, `timezone` `Asia/Jakarta`, `dateFormat` `dd/MM/yy`, `timeFormat` `HH:mm`, `sessionIdleTimeout` `30` |

- Tidak ada state global yang diubah. Suite berjalan serial (`parallel: false`).
- Layar awal Global Settings > General Settings dibuka di hook `beforeEach` (konvensi bagian 4); spec ini tidak memakainya.

## Test Steps

### TC-GS-GSET-124, TC-GS-GSET-125, TC-GS-GSET-126: PUT langsung oleh Read Only, System Role, dan Capability Individual ditolak

1. Untuk setiap baris tabel "PUT langsung" (urutan 1 sampai 3), lakukan langkah 2 sampai 6 dengan aktor baris itu
2. Ganti ke sesi API aktor baris itu
3. Kirim PUT `/v2/enterprise-management/general-settings` dengan payload valid (Session Idle Timeout `60`) memakai token aktor
4. Verifikasi respons `403` `Forbidden`
5. Ganti ke sesi API TC-A, lalu kirim GET `/v2/enterprise-management/general-settings`
6. Verifikasi `sessionIdleTimeout` pada respons GET tetap `30` (Session Idle Timeout tersimpan `30 minutes`, tidak berubah)

### TC-GS-GSET-127, TC-GS-GSET-128, TC-GS-GSET-129: GET langsung oleh System Role, Capability Individual, dan Read Only

7. Untuk setiap baris tabel "GET langsung" (urutan 1 sampai 3), lakukan langkah 8 sampai 11 dengan aktor dan nilai baris itu
8. Ganti ke sesi API aktor baris itu
9. Kirim GET `/v2/enterprise-management/general-settings` memakai token aktor
10. Verifikasi status respons sesuai kolom Status
11. Verifikasi isi respons sesuai kolom Isi respons

### TC-GS-GSET-130: PUT langsung saat entitas suspended ditolak walau aktor Total Control

12. Ganti ke sesi API TC-S, lalu kirim PUT `/v2/enterprise-management/general-settings` dengan payload valid (Session Idle Timeout `60`)
13. Verifikasi respons `403` `Forbidden`
14. Kirim GET `/v2/enterprise-management/general-settings` memakai token TC-S
15. Verifikasi `sessionIdleTimeout` pada respons GET tetap `30` (Session Idle Timeout tersimpan `30 minutes`, tidak berubah)

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (TC-GS-GSET-124 sampai TC-GS-GSET-130). Mode: FE+BE. Kelas: defense-in-depth (direct API tampering, prinsip 13 butir a).
- TC-GS-GSET-130 adalah satu-satunya TC kelas h (write-lockdown entitas Suspended) di spec ini (`P-5` (b)): objek uji ringan (satu PUT ditolak dan satu GET), tanpa state berat sendiri, dan record `Client Suspended` (Pre-setup No 16) hanya dibaca.
- Langkah berulang (bagian 8b butir 7): langkah 2 sampai 6 diulang tiga kali dan langkah 8 sampai 11 tiga kali; ekspansi 1 + 5 x 3 + 1 + 4 x 3 + 4 = 33 langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 3, 5, 7, 8, 9, 12, dan 14 (ganti sesi API dan mengirim request); langkah 5 dan 14 membaca state data lewat GET (data state, bagian 8b butir 1).
- Nilai tersimpan diamati lewat GET dengan token TC-A (langkah 5) atau token TC-S (langkah 14), bukan lewat sesi SR atau CI atau RO di UI. Cara ini sesuai langkah 2 TC-GS-GSET-125 dan TC-GS-GSET-126 (GET dengan token Total Control, karena halaman ditolak 403 untuk aktor itu, TC-GS-GSET-26 dan 27). TC-GS-GSET-124 diseragamkan dengan cara yang sama walau Read Only dapat membuka halaman.
- Kemampuan membaca nilai tersimpan `Client Suspended` untuk TC-GS-GSET-130 memakai GET dari staf entitas itu sendiri; GET dibolehkan saat suspended (TC-GS-GSET-56).
- Dependensi TC-GS-GSET-124 sampai TC-GS-GSET-130 adalah "-" pada TC.
- Temuan untuk QA:
  - TC-GS-GSET-130 langkah 2 ("Buka General Settings dan amati nilai") tidak menyebut akun pengamat; spec memakai GET dari staf `Client Suspended`. Email dan password akun staf `Client Suspended` serta record General Settings entitas itu tidak tertulis di Pre-setup TC; disediakan tim FE.
  - Penamaan env var `GS_GSET_RO_PASSWORD`, `GS_GSET_SR_PASSWORD`, dan `GS_GSET_CI_PASSWORD` baru; nama `GS_RO_PASSWORD` yang sudah ada di `.env.example` merujuk akun Read Only suite Brand (`readOnly_automated_qaTeam1`), bukan akun Pre-setup GSET.

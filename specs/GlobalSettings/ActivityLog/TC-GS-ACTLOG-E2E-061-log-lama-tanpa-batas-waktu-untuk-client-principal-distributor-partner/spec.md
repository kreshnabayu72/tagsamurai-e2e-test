---
id: TC-GS-ACTLOG-E2E-061-log-lama-tanpa-batas-waktu-untuk-client-principal-distributor-partner
title: "Log Lama Tanpa Batas Waktu untuk Client, Principal, Distributor, Partner"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-225
coverage:
  web: automated
---

# Log Lama Tanpa Batas Waktu untuk Client, Principal, Distributor, Partner

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (Total Control tiap entitas):

| Entitas | Akun Total Control | Kredensial |
|---|---|---|
| Client | Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| Principal | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_PRINCIPAL_TC_PASSWORD` |
| Distributor | `totalControlDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_DISTRIBUTOR_TC_PASSWORD` |
| Partner | Total Control Partner (`Fixture.activityLog.partnerTC`): disediakan tim FE (fixture baru), nama env diusulkan: `GS_PARTNER_TC_PASSWORD`; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example` | `Spectra.env.GS_PARTNER_TC_PASSWORD` |

- Login entitas pertama (Client) di hook `before`; entitas berikutnya lewat langkah ganti akun eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md) untuk akun aktor suite.
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun Total Control Principal, Distributor, dan Partner dan halaman Activity Log (kemampuan disediakan tim FE/BE).
- Data Pre-setup: keempat entitas ada di environment.
- Data Dinamis dan kemampuan teknis (disediakan tim FE/BE; kelas volume data khusus: retensi lintas tahun): seed BE pada tiap entitas berupa satu entri Session dan satu entri User Action bertanggal tiga tahun sebelum tanggal run, tanpa mengarang endpoint. Penanda unik `Log Lama {runId}-061` ditulis pada kolom Note untuk entri Session dan pada kolom Name untuk entri User Action. Entri log bersifat tetap dan tidak dapat dihapus; pembersihan entri seed tidak berlaku. Tanggal entri lama dibaca dari hasil seeding, bukan dihitung dari tanggal run.
- Suite serial (`parallel: false`) mengikuti `suite.md`; sesi dikembalikan ke akun default suite di hook `after`.

## Test Steps

### TC-GS-ACTLOG-225: Log lama tetap tampil tanpa batas waktu

Untuk setiap baris tabel "Role yang diuji" (Client, Principal, Distributor, Partner), lakukan langkah 1 sampai 11. Langkah 1 dilewati untuk Client karena sudah login di hook `before`.

1. Ganti akun: login sebagai Total Control entitas yang sedang diuji
2. Buka Global Settings > Activity Log > Session
3. Klik icon Filter, isi field Date dengan rentang yang memuat tanggal entri Session lama hasil seeding, klik [Apply]
4. Verifikasi entri Session dengan Note `Log Lama {runId}-061` tampil di Tab Session
5. Verifikasi tidak ada pesan batas retensi di Tab Session
6. Klik icon Filter, klik [Clear Field] pada field Date, klik [Apply]
7. Klik tab "User Action"
8. Klik icon Filter, isi field Date dengan rentang yang memuat tanggal entri User Action lama hasil seeding, klik [Apply]
9. Verifikasi entri User Action dengan Name `Log Lama {runId}-061` tampil di Tab User Action
10. Verifikasi tidak ada pesan batas retensi di Tab User Action
11. Klik icon Filter, klik [Clear Field] pada field Date, klik [Apply]

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Kelas harness e (volume data khusus, retensi lintas tahun). Spec mengikuti pola Role Matrix: langkah 1 sampai 11 identik untuk setiap entitas; hanya akun login yang berbeda.
- Spec di atas smell 35 langkah dengan ekspansi: 11 langkah nominal, 43 langkah dieksekusi (langkah 1 sampai 11 dikali empat entitas, dikurangi langkah 1 untuk Client). Alasan: semua blok satu kelas harness dan identik per entitas; hanya akun login yang berbeda dan kegagalan satu entitas tidak membuat entitas lain kehilangan makna.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (ganti akun eksplisit, S-07), langkah 6 dan 11 (membersihkan Filter Date).
- Penanda `Log Lama {runId}-061` membedakan entri seed run ini dari entri lama run sebelumnya yang jatuh di rentang Date yang sama (log append-only).
- Pembagian TC lintas spec: TC-GS-ACTLOG-222 dan 223 ada di spec 059; TC-GS-ACTLOG-224 di spec 060.
- Temuan untuk QA:
  - PRD belum menetapkan apakah Filter Panel menutup sesudah [Apply]; langkah klik icon Filter pada langkah 6 dan 11 mengikuti TC-GS-ACTLOG-225.
  - Akun Total Control Partner belum ada di `.env.example`; email disediakan tim FE (fixture baru), diusulkan env `GS_PARTNER_TC_PASSWORD`.
  - TC-GS-ACTLOG-225 menyebut entri bertanggal tiga tahun lalu tanpa nama atau Action yang dapat dicari; spec memakai penanda `Log Lama {runId}-061` pada kolom Note (Session) dan Name (User Action) yang disediakan seed BE.
  - TC-GS-ACTLOG-225 tidak menyebut bahwa kontrol Date Filter menerima tanggal tiga tahun lalu; bila rentang itu tidak dapat dipilih, TC tidak dapat dijalankan.
  - Entri seed log tidak dapat dibersihkan (log append-only, ACTLOG-LOGIC-01); tim BE menentukan cara menyeed ulang tanpa menumpuk entri antar run.
  - Kolom Automation TC-GS-ACTLOG-225 `Manual Only`; spec tetap ditulis dengan kebutuhan teknis di Prerequisites.

---
id: TC-AC-LCS-E2E-186-tooltip-label-field-client-lifecycle
title: "Tooltip Label Field Tab Client Lifecycle"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-43
coverage:
  web: automated
---

# Tooltip Label Field Tab Client Lifecycle

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE); hover pada label field.
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-43: Tooltip label field tab Client Lifecycle menampilkan teks sesuai spesifikasi

1. Klik tab Client Lifecycle pada tab bar
2. Hover label "Notify Plan Owner Before Event"
3. Verifikasi Tooltip pada label "Notify Plan Owner Before Event": "Number of days before expiry/downgrade when an in-app notification is sent to the parties responsible for this client's subscription (Partner/Distributor/Principal, per the client's ownership chain) — separate from the Client-facing reminders below. Not tied to those reminder timings; set independently."
4. Hover label "First Reminder Before Event"
5. Verifikasi Tooltip pada label "First Reminder Before Event": "Number of days before expiry/downgrade when the first reminder email is sent. For expiry, the renewal reminder banner also starts to appear on the License page. For downgrade, this also enables the Wizard Reconciliation."
6. Hover label "Second Reminder Before Event"
7. Verifikasi Tooltip pada label "Second Reminder Before Event": "Number of days before the event when the second reminder email is sent and the renewal reminder banner on the License page escalates."
8. Hover label "Final Reminder Before Event"
9. Verifikasi Tooltip pada label "Final Reminder Before Event": "Number of days before the event when the final reminder email is sent and the renewal reminder banner on the License page escalates."
10. Hover label "Grace Period Duration"
11. Verifikasi Tooltip pada label "Grace Period Duration": "Number of days after expiry/downgrade where data remains in warm storage (read-only, instant access). Client can recover by renewing/upgrading during this period."
12. Hover label "Archive Period Duration"
13. Verifikasi Tooltip pada label "Archive Period Duration": "Number of days after Grace Period where data is in cold storage. Retrieval requires support request (~24h). After this period, the subscription is purged."
14. Hover label "Purge Warning Email"
15. Verifikasi Tooltip pada label "Purge Warning Email": "Number of days before the subscription is purged when a warning email is sent to the client."
16. Hover label "Purge Urgent Warning Email"
17. Verifikasi Tooltip pada label "Purge Urgent Warning Email": "Number of days before the subscription is purged when an urgent warning email is sent."
18. Hover label "Post-Purge Retention"
19. Verifikasi Tooltip pada label "Post-Purge Retention": "Number of days after Hard Purge that a data snapshot is retained in a separate cold archive, restorable only via manual Support/Principal request. After this period, the archive is permanently and irreversibly deleted."

## Notes

- Langkah penghubung (S-03): klik tab Client Lifecycle (TC memulai dari tab itu menurut Precondition). Tiap tooltip diasersi tepat setelah hover label-nya (bagian 8b butir 5). Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Langkah hover diulang per label (langkah 2, 4, 6, 8, 10, 12, 14, 16, 18); satu `Verifikasi` per tooltip (S-01).
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).

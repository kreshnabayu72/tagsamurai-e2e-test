---
id: TC-AC-SU-E2E-037-detail-user-tab-user-log-sesi-admin-console-dan-export
title: "Detail User Tab User Log (riwayat sesi Admin Console): 6 kolom baku, Filter Date, event force-logout, dan export CSV"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-240
  - TC-AC-SU-241
  - TC-AC-SU-242
  - TC-AC-SU-244
  - TC-AC-SU-245
  - TC-AC-SU-246
coverage:
  web: automated
---

# Detail User Tab User Log (riwayat sesi Admin Console): 6 kolom baku, Filter Date, event force-logout, dan export CSV

## Prerequisites

- Login sebagai Role: Principal Total Control
- Target pengguna pernah login ke Admin Console dan memiliki riwayat sesi

## Test Steps

### Screening Tab User Log dan Struktur Kolom Log Baku

1. Buka Detail User > Tab `User Log`
2. Verifikasi tabel memuat 6 kolom log baku: `Date`, `Activity`, `Status`, `Note`, `IP Address`, `Device / Browser` tanpa trigger Column Visibility
3. Verifikasi nilai pada kolom Activity selalu bernilai literal `"Session"` dan kolom Status selalu bernilai `"—"`
4. Buka Filter Panel di Tab User Log, verifikasi hanya filter rentang tanggal (Date Range Picker) yang ditawarkan (tanpa filter Activity / Status)

### Verifikasi Event Force-Logout dan Export

1. Lakukan Deactivate pada pengguna yang sedang memiliki sesi aktif
2. Buka kembali Tab User Log pengguna tersebut
3. Verifikasi entri sesi baru tercatat dengan Activity `"Session"`, Status `"—"`, dan Note `"Session ended"`
4. Klik tombol `[Download]`, verifikasi file terunduh dengan nama `User-Log-[User Name].csv`

### Verifikasi Empty State Pengguna Baru

1. Buka Tab User Log pada pengguna berstatus Pending Activation yang belum pernah login ke portal
2. Verifikasi tabel menampilkan ilustrasi dan pesan empty state: Title `"No sessions recorded"` dan Description `"Session activity will appear here."`

## Notes

- Tab User Log menyajikan dossier riwayat sesi autentikasi pengguna pada portal Admin Console.

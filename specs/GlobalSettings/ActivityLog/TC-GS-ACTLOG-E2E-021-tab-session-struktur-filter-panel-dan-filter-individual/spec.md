---
id: TC-GS-ACTLOG-E2E-021-tab-session-struktur-filter-panel-dan-filter-individual
title: "Tab Session: Struktur 6 Field Filter Panel, Logika OR Intra-Field, Logika AND, dan Filter Date"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-66
  - TC-GS-ACTLOG-67
  - TC-GS-ACTLOG-68
  - TC-GS-ACTLOG-69
  - TC-GS-ACTLOG-70
  - TC-GS-ACTLOG-71
  - TC-GS-ACTLOG-74
  - TC-GS-ACTLOG-75
  - TC-GS-ACTLOG-76
  - TC-GS-ACTLOG-77
coverage:
  web: automated
---

# Tab Session: Struktur 6 Field Filter Panel, Logika OR Intra-Field, Logika AND, dan Filter Date

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat data log Session dengan variasi Date, User, Position, Division, Activity, Status

## Test Steps

### Struktur Filter Panel Tab Session
1. Buka Tab Session, klik icon Filter di toolbar.
2. Verifikasi Filter Panel terbuka dengan icon Filter berubah gelap.
3. Verifikasi 6 field tampil berurutan: Date, User, Position, Division, Activity, Status.
4. Verifikasi footer panel menyediakan tombol [Clear Field] di kiri dan [Apply] di kanan.
### Logika OR Intra-Field & Status Dash
5. Pada field Activity, pilih dua opsi: 'Login' dan 'Logout', lalu klik [Apply].
6. Verifikasi tabel menampilkan baris dengan Activity Login ATAU Logout (logika OR).
7. Buka kembali filter, pilih Status = 'Failed', klik [Apply].
8. Verifikasi baris Login Failed tampil, namun baris Logout dan Session (yang Status-nya tampil '—') TIDAK tampil.
### Logika AND Antar-Field
9. Pilih Activity 'Login' DAN Status 'Failed', klik [Apply].
10. Verifikasi hanya baris yang memenuhi kedua kriteria (Login AND Failed) yang tampil.
11. Terapkan kombinasi multi-opsi: Activity (Login + Reset Password) DAN Status (Failed), verifikasi hasil irisan tepat.
### Aturan Filter Date (Date Range Picker)
12. Filter Date dengan rentang 14 Jul 2026 s/d 14 Jul 2026, verifikasi batas inklusif dari 00:00:00 hingga 23:59:59.
13. Verifikasi perbandingan rentang tanggal dievaluasi berdasarkan zona waktu General Settings.
14. Buka picker Date, pilih tanggal mulai 14 Jul 2026, coba pilih tanggal akhir 10 Jul 2026, verifikasi tanggal sebelum mulai tidak dapat dipilih.
15. Isi hanya tanggal mulai saja, klik [Apply], verifikasi menyaring dari tanggal tersebut ke atas.
16. Isi hanya tanggal akhir saja, klik [Apply], verifikasi menyaring sampai tanggal tersebut.

## Notes

- Logika filter multi-dimensi menggabungkan OR intra-field dan AND antar-field secara presisi.

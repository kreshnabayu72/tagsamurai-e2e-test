---
id: TC-GS-GSET-E2E-029-changelog-kolom-date-format-self-reference-hover-modified-by-dan-old-new-utuh
title: "Kolom Changelog: Date mengikuti Date/Time Format (self-reference), hover Modified By nama lengkap, Old/New Value utuh, dan pergeseran jam akibat Time Zone"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-GSET-103
  - TC-GS-GSET-161
  - TC-GS-GSET-162
  - TC-GS-GSET-163
coverage:
  web: automated
---

# Kolom Changelog: Date mengikuti Date/Time Format (self-reference), hover Modified By nama lengkap, Old/New Value utuh, dan pergeseran jam akibat Time Zone

## Prerequisites

- Login sebagai Role: Total Control
- Changelog General Settings berisi baris riwayat (dinamis) termasuk baris Field `Time Zone` dan Field `Session Idle Timeout` oleh Budi Santoso
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`

## Test Steps

### Date Self-Reference

1. Pilih Date Format `M/d/yy` dan Time Format `hh:mm a`, lalu klik `[Save]`
2. Buka Modal Changelog dan amati kolom Date
3. Verifikasi kolom Date menampilkan tanggal berformat `M/d/yy` (bulan dan hari tanpa angka nol di depan) dan waktu berformat `hh:mm a` (12 jam dengan AM/PM) pada seluruh baris

### Hover Modified By Nama Lengkap

4. Hover nilai `Budi S` pada kolom Modified By
5. Verifikasi tooltip menampilkan nama lengkap `Budi Santoso`

### Old Value/New Value Utuh

6. Buka Modal Changelog dan cari baris Field `Time Zone`
7. Amati kolom Old Value dan New Value pada baris itu
8. Verifikasi keduanya menampilkan label opsi Time Zone secara utuh tanpa karakter pemotong ".." dan kolom melebar mengikuti konten
9. Hover nilai pada kolom Old Value dan verifikasi tidak memunculkan tooltip

### Pergeseran Jam akibat Time Zone

10. Catat jam pada baris Field `Session Idle Timeout` kolom Date di Modal Changelog
11. Tutup modal, pilih Time Zone Lain (offset berbeda dari `Asia/Jakarta`, dihitung dari label (UTC±HH:MM)), lalu klik `[Save]`
12. Buka Modal Changelog dan baca jam baris yang sama
13. Verifikasi jam bergeser sebesar selisih offset standar antara label `Asia/Jakarta` dan Time Zone Lain
14. Verifikasi tanggal ikut berubah bila pergeseran melewati tengah malam, sedangkan format Date Format dan Time Format tidak berubah

## Notes

- Menggabungkan TC-GS-GSET-103, 161, 162, dan 163 (kolom Changelog: Date, hover, Old/New Value, pergeseran Time Zone). Langkah 11–12 menambah baris Field `Time Zone` baru di Changelog.

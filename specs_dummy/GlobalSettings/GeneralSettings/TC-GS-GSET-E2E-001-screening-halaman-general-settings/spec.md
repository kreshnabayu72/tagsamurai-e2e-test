---
id: TC-GS-GSET-E2E-001-screening-halaman-general-settings
title: "Screening halaman General Settings: breadcrumb, tiga SectionCard, kontrol form, dan footer"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-01
coverage:
  web: automated
---

# Screening halaman General Settings: breadcrumb, tiga SectionCard, kontrol form, dan footer

## Prerequisites

- Login sebagai Role: Total Control
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`

## Test Steps

1. Buka Global Settings > General Settings
2. Verifikasi breadcrumb menampilkan teks "General Settings" sebagai segmen tunggal, aktif, dan tidak dapat diklik
3. Verifikasi icon button Changelog tampil di pojok kanan atas halaman dan merupakan satu-satunya toolbar icon
4. Verifikasi body tersusun atas tiga SectionCard terpisah: "Currency", "Date & Time", dan "Security"
5. Verifikasi SectionCard "Currency" memuat Select varian Searchable "Currency Code" dengan ikon info dan Preview text "Rp 5.000,00"
6. Verifikasi SectionCard "Date & Time" memuat Select "Date Format" (`dd/MM/yy`), Select "Time Format" (`HH:mm`), Select varian Searchable "Time Zone" dengan ikon info (`Asia/Jakarta`), dan Preview text "17/03/23 14:30"
7. Verifikasi SectionCard "Security" memuat Select "Session Idle Timeout" dengan ikon info (`30 minutes`)
8. Verifikasi tidak ada field "Currency Symbol" maupun "Decimal Places", tidak ada tombol `[Clear Field]`, dan tidak ada placeholder "-- Select --"
9. Verifikasi tombol "Save" berwarna success menempel di bawah halaman dengan status disabled, dan tidak ada tombol Cancel

## Notes

- Screening halaman tanpa aksi, ditaruh di awal sesuai urutan read-only → edit → changelog (TC-GS-GSET-01).

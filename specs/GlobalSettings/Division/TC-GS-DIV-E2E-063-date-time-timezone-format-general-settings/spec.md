---
id: TC-GS-DIV-E2E-063-date-time-timezone-format-general-settings
title: "Konsistensi Format Tanggal dan Waktu Mengikuti Konfigurasi General Settings"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-174
  - TC-GS-DIV-175
  - TC-GS-DIV-176
  - TC-GS-DIV-177
coverage:
  web: automated
---

# Konsistensi Format Tanggal dan Waktu Mengikuti Konfigurasi General Settings

## Prerequisites

- Login sebagai Role: Total Control
- Format tanggal pada General Settings telah diatur ke pola standar (misal DD/MM/YYYY)

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Amati nilai pada kolom 'Last Updated' pada tabel utama
3. Verifikasi format tanggal dan waktu yang ditampilkan sesuai dengan konfigurasi General Settings entitas
4. Buka Filter Panel tabel utama dan periksa input DateRangePicker
5. Verifikasi format tanggal pada pemilih tanggal selaras dengan format sistem
6. Buka Modal Changelog Division dan amati kolom 'Date'
7. Verifikasi format timestamp event changelog mengikuti aturan General Settings
8. Periksa filter 'Date' pada Filter Panel Changelog dan verifikasi format tanggal konsisten

## Notes

- Memastikan kepatuhan format datetime platform terhadap modul General Settings (prd-conventions.md §32).

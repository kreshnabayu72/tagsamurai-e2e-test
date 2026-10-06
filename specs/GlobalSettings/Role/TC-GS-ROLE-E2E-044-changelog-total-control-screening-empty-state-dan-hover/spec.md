---
id: TC-GS-ROLE-E2E-044-changelog-total-control-screening-empty-state-dan-hover
title: "Screening Modal Changelog Tab Total Control, Tampilan Empty State, dan Hover Tooltip"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-78
  - TC-GS-ROLE-116
  - TC-GS-ROLE-209
coverage:
  web: automated
---

# Screening Modal Changelog Tab Total Control, Tampilan Empty State, dan Hover Tooltip

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia data riwayat log pada Tab Total Control

## Test Steps

1. Buka Global Settings > Role & Permission > Tab Total Control
2. Klik icon Changelog (⏱) pada toolbar tabel
3. Verifikasi modal Changelog terbuka dengan judul: "Changelog: Role & Permission > Total Control"
4. Verifikasi tabel Changelog memuat 7 kolom data: Date, Action, User Name, Field, Old Value, New Value, Modified By
5. Simulasikan kondisi riwayat log kosong pada modal Changelog (mode mock)
6. Verifikasi tampilan empty state muncul dengan Title: "No changelog yet" dan Description: "Activities and changes will appear here."
7. Arahkan kursor mouse (hover) pada nama Modified By atau sel teks yang terpotong
8. Verifikasi tooltip muncul menampilkan nilai teks lengkap

## Notes

- Modal Changelog Tab Total Control mencatat riwayat mutasi penugasan dan pencabutan Total Control (role.md §8.1).

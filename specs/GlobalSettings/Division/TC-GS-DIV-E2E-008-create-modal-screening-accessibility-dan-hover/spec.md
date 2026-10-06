---
id: TC-GS-DIV-E2E-008-create-modal-screening-accessibility-dan-hover
title: "Screening Modal Create Division, Atribut Aksesibilitas, dan Feedback Tombol"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-15
  - TC-GS-DIV-16
  - TC-GS-DIV-17
  - TC-GS-DIV-194
coverage:
  web: automated
---

# Screening Modal Create Division, Atribut Aksesibilitas, dan Feedback Tombol

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Klik tombol '[+ Division]' pada toolbar
3. Verifikasi modal dialog 'Create Division' terbuka dengan icon close '[✕]' di kanan atas
4. Verifikasi field 'Division Name *' memiliki placeholder 'Enter division name', kursor otomatis fokus pada input ini, atribut aria-required bernilai true, dan max length 120
5. Verifikasi field 'Code' bersifat opsional dengan placeholder 'Enter code, or leave blank to auto-generate', helper text 'Letters, numbers, hyphens, underscores, and dots only' selalu tampil, dan max length 15
6. Verifikasi checkbox 'Stay on this form after submitting' berstatus tidak tercentang (unchecked secara default)
7. Verifikasi footer modal memuat tombol '[Clear Field]' (variant text) dan '[Submit]' (variant filled primary) tanpa tombol Cancel terpisah
8. Arahkan kursor (hover) pada tombol '[Submit]' dan '[Clear Field]' lalu verifikasi perubahan visual hover state
9. Tekan tombol Tab berulang kali dan verifikasi fokus keyboard terperangkap di dalam modal (focus trap)
10. Tekan tombol Escape (Esc) dan verifikasi modal Create Division menutup dengan bersih

## Notes

- Mengacu pada spesifikasi form modal division.md §4.2c dan standar aksesibilitas §4.5.

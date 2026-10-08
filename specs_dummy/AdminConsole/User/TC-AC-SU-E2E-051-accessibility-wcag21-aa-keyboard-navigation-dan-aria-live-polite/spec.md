---
id: TC-AC-SU-E2E-051-accessibility-wcag21-aa-keyboard-navigation-dan-aria-live-polite
title: "Aksesibilitas WCAG 2.1 AA: Navigasi Keyboard Penuh, Focus Trap, dan ARIA-Live Polite"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-196
  - TC-AC-SU-197
  - TC-AC-SU-198
coverage:
  web: automated
---

# Aksesibilitas WCAG 2.1 AA: Navigasi Keyboard Penuh, Focus Trap, dan ARIA-Live Polite

## Prerequisites

- Login sebagai Total Control
- Berada pada halaman User List

## Test Steps

### Navigasi Papan Ketik (Keyboard Only)
1. Gunakan tombol keyboard `Tab` dan `Shift+Tab` untuk berpindah antar elemen interaktif
2. Verifikasi outline fokus (focus ring) tampak jelas pada tiap elemen dengan rasio kontras >= 4.5:1
3. Pindahkan fokus ke tabel data; gunakan tombol panah `Arrow Up / Down` untuk navigasi baris
4. Fokuskan ke switch Active baris; tekan tombol `Space` untuk memicu dialog konfirmasi
5. Tekan tombol `Enter` untuk mengeksekusi aksi

### Verifikasi Focus Trap pada Modal Dialog
6. Saat modal dialog konfirmasi terbuka, tekan tombol `Tab` berulang kali
7. Verifikasi siklus fokus terkunci (focus trap) di dalam elemen modal (`[Cancel]`, tombol eksekusi, tombol silang ✕) dan tidak dapat melompat ke konten latar belakang halaman
8. Tekan tombol keyboard `Esc` untuk menutup modal dialog secara aksesibel

### Verifikasi Kepatuhan Screen Reader ARIA Live
9. Picu kemunculan pesan kesalahan form atau toast notifikasi sukses
10. Verifikasi container elemen notifikasi memiliki atribut `aria-live="polite"` atau `role="status"` sehingga terbaca oleh perangkat screen reader

## Notes

Memenuhi standar kepatuhan aksesibilitas web internasional WCAG 2.1 Level AA.
